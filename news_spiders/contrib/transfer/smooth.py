"""
This module is suitable for the transfer files between machine, win is local, linux is remote
mainly operate to push file from win to linux, But this operation method is a bit awkward
"""
import logging
import paramiko

from .base import Base

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class SmoothTransfer(Base):
    """
    Use paramiko module require three packages
    1:windows to linux, as follow blew:
        `MinGW`: windows system , add 'xx\MinGW\bin' to os path
        `PyCrypto`: install pycrypto, before install paramiko
        `paramiko`: install
        Note: if only `Authentication failed` Error, maybe `username` or `passwd` is incorrect.
    2:linux to linux: paramiko and pexpect packages
        details can reference the related document with Internet.
    """
    def __init__(self, host=None, port=22, user=None, password=None):
        super(SmoothTransfer, self).__init__()

        self._host = host or self.inner_host
        self._port = port or self.inner_port
        self._user = user or self.inner_user
        self._pwd = password or self.inner_pwd

    def ssh_command(self, cmd, echo=False):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self._host, self._port, self._user, self._pwd, timeout=10)

            stdin, stdout, stderr = client.exec_command(cmd)
            if echo:
                logger.info('\nCmd <{}>: stdout: \n\t{}'.format(cmd, '\t'.join([f for f in stdout])))
        except Exception as e:
            logger.info('\n\tRun error: cmd <{}>, type <{}>, info <{}>'.format(cmd, e.__class__, e))
        finally:
            client.close()

    @property
    def sftp(self):
        sock = (self._host, self._port)
        t = paramiko.Transport(sock=sock)
        t.connect(username=self._user, password=self._pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        return sftp

    def put(self, local_path, remote_path, disc_key=True):
        """
        :param local_path: Absolutely local path. eg: abc.txt
        :param remote_path: Absolutely server path. eg: /home/daily_news/scf_news/abc.txt
        :param disc_key: bool
        """
        try:
            sftp = self.sftp
            sftp.put(local_path, remote_path)
            sftp.close()
        except Exception as e:
            logger.info('\n\tPut file error: cmd <{}>, type <{}>, info <{}>'.format(e.__class__, e))

    def get(self, local_path, remote_path):
        try:
            sftp = self.sftp
            sftp.get(local_path, remote_path)
            sftp.close()
        except Exception as e:
            logger.info('\n\tGet file error: cmd <{}>, type <{}>, info <{}>'.format(e.__class__, e))

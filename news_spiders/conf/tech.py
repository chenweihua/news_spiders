# -*- coding: utf-8 -*-
"""
该配置主要解决各类网站的科技类新闻的配置
"""

import re

TECH_CONFIGS = [
    {
        'site': 'tech_qq',
        'urls': [
            {
                'page_url': 'http://tech.qq.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '_%s', 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/c/recodelist_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://bi.qq.com/c/bi2_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/c/tnw_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://digi.tech.qq.com/c/yinkeji_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://digi.tech.qq.com/c/theverge_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/c/zmt_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/web/lCompany.htm%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/web/newWy.htm%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/c/dzsw_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/web/intelligent.htm%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://digi.tech.qq.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/c/ydhl_%s.htm',
                'pages': 14, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/c/tx_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/c/it_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/c/hlwdj_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'block_attr':   ('div[class="jdtdBg"]', 'div[class="fonta"]', 'a.pic', 'div.pic',
                         'h3[class="f18 l26"] a',),
        'remove_tags': ('.pictext', '#invideocon', '#relInfo', '.hqimg_related', 'script', 'style'),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('.pubTime', ),
                    'auth': ('.where', )
                },
                'pyq_content':  ('#Cnt-Main-Article-QQ', )
            }
    },

    {
        'site': 'tech_ifeng',
        'urls': [
            {
                'page_url': 'http://tech.ifeng.com/%s', 'pages': 1,
                'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.ifeng.com/listpage/800/0/%s/rtlist.shtml', 'pages': 1,
                'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.ifeng.com/listpage/803/%s/list.shtml', 'pages': 1,
                'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.ifeng.com/listpage/26333/%s/list.shtml', 'pages': 1,
                'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.ifeng.com/listpage/26335/%s/list.shtml', 'pages': 1,
                'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.ifeng.com/listpage/26334/%s/list.shtml', 'pages': 1,
                'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'block_attr':   ('div.box01_hots.m01', 'div#morenews1', 'div#box_content', 'h3[class="text-tit"]'),
        'remove_tags': ('.picIntro', 'dov.cmt',),
        'details':
            {
                'pyq_title':        ('#artical_topic', ),  # must this module
                'pyq_date_author':  {
                    'date': ('.ss01', ('div#artical_sth', 'span', 0)),
                    'auth': ('.ss03', 'div#artical_sth a[ref="nofollow"]',
                             'div#artical_sth span#source_place', ('div#artical_sth', 'p', 0)),
                },  # must this module
                'pyq_content':      ('#main_content', 'div#artical_real')  # must this module
            }
    },

    {
        'site': 'tech_sina',
        'urls': [
            {
                'page_url': 'http://tech.sina.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://chuangye.sina.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.sina.com.cn/internet/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'block_attr':   ('#impNews1', 'h2[class="undefined"] a', 'div[class="p"]'),
        'remove_tags': ('.img_descr', 'div[data-sudaclick="suda_1028_guba"]', '#sinashareto',
                        '.finance_app_zqtg',  '.hqimg_related', '.otherContent_01'),
        'details':
            {
                'pyq_title':        ('#artibodyTitle', '#main_title'),
                'pyq_date_author':  {
                    'date': ('.time-source', '#pub_date'),
                    'auth': ('.time-source', 'span[data-sudaclick="media_name"]', '#media_name')
                },
                'pyq_content':  (re.compile(r'<!-- publish_helper.*?>(.*?)<!-- publish_helper_end -->', re.S),
                                 '#artibody')
            }
    },

    {
        'site': 'tech_qianzhan',
        'urls': [
            {
                'page_url': 'http://t.qianzhan.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'multi_page':   ('.page',),
        'block_attr':   ('.pic', 'p.f22'),
        'remove_tags': ('p[style="padding-top:0px; font-style:italic;"]', 'i', 'div[class="mt30"]',
                        'style', 'script'),
        'details':
            {
                'pyq_title':        ('#h_title', 'h1'),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', '.content_info'),
                    'auth': ('#source_baidu', '.content_info')
                },
                'pyq_content':  ('#div_content', '#content', 'div[class="art"]')
            }
    },

    {
        'site': 'tech_china',
        'urls': [
            {
                'page_url': 'http://tech.china.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            # 科技
            {
                'page_url': 'http://app.tech.china.com.cn/news/my.php?cname=%E7%A7%91%E6%8A%80&p=%s',
                'pages': 38, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            # 互联网
            {
                'page_url': 'http://app.tech.china.com.cn/news/column.php?cname=%E4%BA%92%E8%81%94%E7%BD%91&p=%s',
                'pages': 344, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            # IT业界
            {
                'page_url': 'http://app.tech.china.com.cn/news/column.php?cname=IT%E4%B8%9A%E7%95%8C&p=%s',
                'pages': 119, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            # 通信
            {
                'page_url': 'http://app.tech.china.com.cn/news/column.php?cname=%E9%80%9A%E4%BF%A1&p=%s',
                'pages': 112, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            # 家电
            {
                'page_url': 'http://app.tech.china.com.cn/news/column.php?cname=%E5%AE%B6%E7%94%B5&p=%s',
                'pages': 75, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            # 创业
            {
                'page_url': 'http://app.tech.china.com.cn/news/column.php?cname=%E5%88%9B%E4%B8%9A&p=%s',
                'pages': 8, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            # 数码
            {
                'page_url': 'http://app.tech.china.com.cn/news/live.php?channel=%E6%95%B0%E7%A0%81&p=%s',
                'pages': 11, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            # 科技滚动新闻
            {
                'page_url': 'http://app.tech.china.com.cn/news/live.php?channel=%E7%A7%91%E6%8A%80&p=%s',
                'pages': 226, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'block_attr':   ('h3.hsTit3', '.news_list'),
        'remove_tags': ('p[align=center]', 'div[class="fr bianj"]'),
        'details':
            {
                'pyq_title':        (('h1', 2), 'h1.toph1'),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', 'span.fl.time2', '.small_one span'),
                    'auth': ('#source_baidu', 'span.fl.time2', ('.small_one', 'a', 0))
                },
                'pyq_content':  ('#content', 'div#fontzoom')
            }
    },

    {
        'site': 'tech_163',
        'urls': [
            {
                'page_url': 'http://tech.163.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.163.com/chuangclub/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.163.com/vr/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.163.com/internet/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.163.com/telecom/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.163.com/it/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://digi.163.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'block_attr': ('div.hb_detail', 'div.hot-list', 'ul[class="newsList"]', 'div.intel_banner',
                       'div.today_hot_news'),
        'remove_tags': (re.compile(r'<!--biaoqian.*?>.*?<!--biaoqian.*?>', re.S),
                        'div[class="ep-source cDGray"]', '.nph_photo', '.nph_photo_ctrl',
                        '.nvt_vote_2', '.demoBox', '.hidden', 'script', 'style'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author': {
                    'date': ('.ep-time-soure', '.post_time_source'),
                    'auth': ("#ne_article_source", )
                },
                'pyq_content':      ('#endText', )
            }
    },

    {
        'site': 'tech_sohu',
        'urls': [
            {
                'page_url': 'http://it.sohu.com/internet%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://it.sohu.com/tele.shtml%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://it.sohu.com/techchanpin/index.shtml%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://mp.sohu.com/profile?xpt=a2VqaXF1YW5qaWFud2VuQHNvaHUuY29t%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'block_attr': ('.lc', '.content-title', 'div.article_left'),
        'remove_tags': ('span[style="font-size: 12px;"]', 'script', 'style'),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author': {
                    'date': ('#pubtime_baidu', ),
                    'auth': ("#media_span", 'span[class="writer"]')
                },
                'pyq_content':      ('[itemprop="articleBody"]', 'div#contentText')
            }
    },

    {
        'site': 'full_36kr',
        'urls': [
            {
                'page_url': 'http://36kr.com/api/info-flow/main_site/posts?column_id=&b_id=5050227&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://36kr.com/api/post?column_id=67&b_id=&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://36kr.com/api/post?column_id=68&b_id=&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://36kr.com/api/post?column_id=23&b_id=&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://36kr.com/api/post?column_id=69&b_id=&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://36kr.com/api/post?column_id=70&b_id=&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://36kr.com/api/post?column_id=71&b_id=5046510&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'json': {
            'data_key': 'data.items',
            'url_key': 'id',
            'date_key': 'published_at',
            'join_key': 'http://36kr.com/p/{url}.html'
        },
        'is_script': True,
        'remove_tags': (),
        'details':
            {
                'pyq_title':        (re.compile(r'"title":"(.*?)","', re.S), ),
                'pyq_date_author':  {
                    'date': (),
                    'auth': ()
                },
                'pyq_content':  (re.compile(r'"content":"(.*?)","', re.S), )
            }
    },

]
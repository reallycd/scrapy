# 北邮人论坛-北邮人的温馨家园

- 原始链接: https://bbs.byr.cn/
- 来源页面: https://tophub.today/
- 状态码: 200

## 抽取文本预览

合作交流

论坛帮助

友情链接

意见建议

忘记密码

<form action="/login" method="post" id="u_login_form"><div class="u-login-input"><input type="text" id="u_login_id" class="input-text input" name="id" placeholder="用户名"/></div><div class="u-login-input"><input type="password" id="u_login_passwd" class="input-text input" name="passwd" placeholder="密码"/></div><div class="u-login-check"><input type="checkbox" id="u_login_cookie" name="CookieDate" value="2"/><label for="u_login_cookie">下次自动登录</label></div><div class="u-login-op"><input type="submit" id="u_login_submit" class="submit" value="登录" /><input class="submit" type="button" value="注册" id="u_login_reg"/></div></form>

<div class="u-login-id"><samp class="ico-pos-cdot"></samp>欢迎<a href="/user/query/<%=id%>" title="<%=id%>"><%=id.length<11?id:(id.substr(0,10)+'...')%></a></div><ul class="u-login-list"><li><a href="/mail" id="m_inbox">我的收件箱<%if (full_mail){%><span class="new_mail">(满!)</span><%}else if(new_mail){%><span class="new_mail">(新)</span><%}%></a></li><%if(typeof new_at !== 'undefined' && false !== new_at){%><li><a href="/refer/at" id="m_at">@我的文章</a><%if(new_at>0){%><span class="new_mail">(<%=new_at%>)</span><%}%></a></li><%}%><%if(typeof new_reply !== 'undefined' && false !== new_reply){%><li><a href="/refer/reply" id="m_reply">回复我的文章</a><%if(new_reply>0){%><span class="new_mail">(<%=new_reply%>)</span><%}%></a></li><%}%><li><a href="/collection" id="u_fav">我的收录文章</a></li><li><a href="/fav" id="u_fav">我的收藏夹</a></li><li><a href="/widget/add">个性首页设置</a></li><li><a href="javascript:void(0)" id="u_login_out">退出登录</a></li></ul>

<ul><li class="slist"><span class="x-folder"><span class="toggler"></span><a href="javascript:void(0);">全部讨论区</a></span><ul class="x-child ajax"><li>{url:/section/ajax_list.json?uid=<%=id%>&root=list-section}</li></ul></li><%if(is_login){ %><li class="flist"><span class="x-folder"><span class="toggler"></span><a href="javascript:void(0);">我的收藏夹</a></span><ul id="list-favor" class="x-child ajax"><li>{url:/f
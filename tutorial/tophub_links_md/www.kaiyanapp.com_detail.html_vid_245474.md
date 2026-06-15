# 开眼-精品短视频

- 原始链接: https://www.kaiyanapp.com/detail.html?vid=245474
- 来源页面: https://tophub.today/
- 状态码: 200

## 抽取文本预览

该作品从地球上消失了

<%if (videoHeadData.isType === 'ugc_picture') {%> <!-- ugc_picture -->
          <img id="ugc-head-pic" class="container-head-pic j-container-head-location" src="<%= videoHeadData.url%>" alt="">
          <div class="container-head-detail j-container-head-detail">
            <p class="detail-head">
              <i class="detail-head-icon" style="background-image: url('<%= videoHeadData.owner.avatar%>')"></i>
              <span class="detail-head-name"><%= videoHeadData.owner.nickname%></span>
            </p>
            <p class="detail-info"><%= videoHeadData.description%></p> <%if (!!videoHeadData.tags) {%> <ul class="detail-tags"> <%for (var i = 0; i < videoHeadData.tags.length; i++) {%> <li class="detail-tags-list"><%= videoHeadData.tags[i].name%></li> <%}%> </ul> <%}%> <%if (!!videoHeadData.description || !!videoHeadData.tags) {%> <div class="container-detail-line"></div> <%}%> <div class="kyt-footer">
  <a href="/"><div class="bottom-logo"></div></a>
  <img src="//static.kaiyanapp.com/eyepetizer-web/assets/images/eyepetizer-wx-qr.9d63f8c1.png" alt="eyepetizer wechat qrcode" />
  <div class="qr-tips">更多丰富内容在「开眼 Eyepetizer」微信公众号</div>
</div>

          </div> <%} else {%> <!-- ugc_video,old_video -->
          <div class="kyt-player j-container-head-location">
            <video webkit-playsinline playsinline="true" preload="none"></video>
            <div class="cover"></div>
            <div class="play-button"></div>
          </div> <%if (videoHeadData.isType === 'ugc_video') {%> <div class="container-head-detail j-container-head-detail">
              <p class="detail-head">
                <i class="detail-head-icon" style="background-image: url('<%= videoHeadData.owner.avatar%>')"></i>
                <span class="detail-head-name"><%= videoHeadData.owner.nickname%></span>
              </p>
              <p class="detail-info"><%= videoHeadData.description%></p> <%if (!!videoHeadData.tags) {%> <ul class="detail-tags"> <%for (var i = 0; i 
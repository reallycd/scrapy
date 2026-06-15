# 注册/登录/今日热榜

- 原始链接: https://tophub.today/login?redirect=%2F%2Ftophub.today%2Fmanage
- 来源页面: https://tophub.today/
- 状态码: 200

## 抽取文本预览

今日热榜

登录后可免费使用热榜订阅、分组管理、热点搜索等高级功能

×

创建账号

注册成为会员，享受更多精彩内容

获取验证码

注册

找回密码

我们将帮助您重置密码

获取验证码

重置密码

欢迎回来

登录您的账号，探索更多精彩内容

或使用账号登录

忘记密码？

登录

欢迎回来！

请登录您的账号，继续探索今日热榜的精彩内容

登录

你好，朋友！

注册成为会员，开启您的热榜之旅

使用社交平台登录无需注册即可体验

注册

登录

注册

找回密码

// 页面切换动画
const container = document.getElementById("container");

document.getElementById("signUp").addEventListener("click", () => {
  container.classList.add("right-panel-active");
  document.getElementById("register").style.display = "block";
  document.getElementById("findpwd").style.display = "none";
});

document.getElementById("findPwd").addEventListener("click", () => {
  container.classList.add("right-panel-active");
  document.getElementById("register").style.display = "none";
  document.getElementById("findpwd").style.display = "block";
});

document.getElementById("signIn").addEventListener("click", () => {
  container.classList.remove("right-panel-active");
});

// 添加输入框焦点效果
const inputGroups = document.querySelectorAll(".input-group");
inputGroups.forEach((group) => {
  const input = group.querySelector("input");
  const icon = group.querySelector("svg");

  if (input && icon) {
    input.addEventListener("focus", () => {
      icon.style.color = "var(--secondary-color)";
    });

    input.addEventListener("blur", () => {
      icon.style.color = "";
    });
  }
});

// 添加按钮点击波纹效果
const buttons = document.querySelectorAll("button");
buttons.forEach((button) => {
  button.addEventListener("click", function (e) {
    const x = e.clientX - e.target.getBoundingClientRect().left;
    const y = e.clientY - e.target.getBoundingClientRect().top;

    const ripple = document.createElement("span");
    ripple.style.cssText = `
      position: absolute;
      background: rgba(255, 255, 255, 0.7);
      transform: translate(-50%, -50%);
      pointer-events: none;
      border-radius: 50%;
      width: 0;
      height: 0;
      left: ${x}px;
      top: ${y}px;
    `;

    button.appendChild(ripple);

    const size = Math.max
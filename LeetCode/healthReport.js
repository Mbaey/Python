// ==UserScript==
// @name        New script
// @namespace   Violentmonkey Scripts
// @match       http://yqtb.nwpu.edu.cn/*
// @grant       none
// @version     1.0
// @author      good guy
// @description 2021/1/4 上午11:28:57 疫情期间自动填报，每日个人健康上报
// ==/UserScript==



(function () {
    "use strict";
    console.log('疫情期间 自动填报');

    // http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp
    window.location.href = "http://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp"
    //点击提交
    // javascript:go_subfx(); 一会儿是 go_subfx，一会儿是 gu_sub()...。
    javascript: go_sub();
    //选中：已核实以上数据，确保真实无误
    $('#brcn').trigger('click');

    scroll(0, document.body.scrollHeight)
    //点击：确认提交
    javascript: save();

    alert("填报成功,去官网看看吧")

    console.log('填报成功');
    // window.location.href="http://www.nwpu.edu.cn"
    //success
    // window.setTimeout("window.location.href='http://www.nwpu.edu.cn'",2000);

    // logout();
    // function logout(){ 
    //   if (confirm("填报成功,去官网看看吧.是-选择确定，否-选择取消"))...{ 
    //     window.location.href="http://www.nwpu.edu.cn" 
    //   } 
    // }
})();
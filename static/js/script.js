/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $("select").formSelect();
    $(".modal").modal();
    $(".genre-row div").hide();
    $(".genre-row div:lt(7)").show();
});
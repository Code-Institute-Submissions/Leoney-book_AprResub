/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $("select").formSelect();
    $(".modal").modal();
    $(".genre-name div").hide();
    $(".genre-name div:lt(6)").show();
});
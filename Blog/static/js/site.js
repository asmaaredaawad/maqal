$(function () {
    $("#btn1").click(function () {
        var z = $("#div1").hasClass("hidden");
        if (z == true) {
            $("#div1").removeClass("hidden")
        } else {
            $("#div1").addClass("hidden")

        }
    });
    $("#btn1").click(function () {
        $("#sp1").addClass("glyphicon-ok");
        return false;
    });
    $("#div1").on("close.bs.alert", function () {
        $("#div1").addClass("hidden")
        return false;
    });
    $("#div2").on("hide.bs.modal", function () {
        $("#divalert").removeClass("hidden")
    });
    $("#divalert").on("close.bs.alert", function () {
        $("#divalert").addClass("hidden");
        return false;});
    $("#cartemp").carousel();
    $('[data-toggle="tooltip"]').tooltip()
})
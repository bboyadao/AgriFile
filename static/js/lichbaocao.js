
$("#div_id_dinhky").hide();

$("#id_kind").on('change', function () {
    css = ""
    var val = $("#id_kind option:selected").val();
    if (val == 1) {
        css = "danger"
        $("#lichbaocao").addClass("card-" + css);
        $("#lichbaocao").removeClass("card-warning");
        $("#lichbaocao").removeClass("card-success");
        $("#lichbaocao").removeClass("card-info");

        $("#lichbaocao_btn").addClass("btn-"+ css);
        $("#lichbaocao_btn").removeClass("btn-warning");
        $("#lichbaocao_btn").removeClass("btn-success");
        $("#lichbaocao_btn").removeClass("btn-info");
    }
    else if (val == 2) {
        css = "warning"
        $("#lichbaocao").addClass("card-" + css);
        $("#lichbaocao").removeClass("card-danger");
        $("#lichbaocao").removeClass("card-success");
        $("#lichbaocao").removeClass("card-info");

        $("#lichbaocao_btn").addClass("btn-"+ css);
        $("#lichbaocao_btn").removeClass("btn-danger");
        $("#lichbaocao_btn").removeClass("btn-success");
        $("#lichbaocao_btn").removeClass("btn-info");
    }
    else if (val == 3) {

        css = "success"
        $("#lichbaocao").addClass("card-" + css);
        $("#lichbaocao").removeClass("card-danger");
        $("#lichbaocao").removeClass("card-warning");
        $("#lichbaocao").removeClass("card-info");

        $("#lichbaocao_btn").addClass("btn-"+ css);
        $("#lichbaocao_btn").removeClass("btn-danger");
        $("#lichbaocao_btn").removeClass("btn-warning");
        $("#lichbaocao_btn").removeClass("btn-info");
    }
    else {
        css = "info"
        $("#lichbaocao").addClass("card-" + css);
        $("#lichbaocao").removeClass("card-danger");
        $("#lichbaocao").removeClass("card-warning");
        $("#lichbaocao").removeClass("card-success");

        $("#lichbaocao_btn").addClass("btn-" + css);
        $("#lichbaocao_btn").removeClass("btn-danger");
        $("#lichbaocao_btn").removeClass("btn-warning");
        $("#lichbaocao_btn").removeClass("btn-success");

    }

    if (this.options[3].selected == true) {
        $("#div_id_dinhky").toggle("slow");
        $("#id_dinhky").prop('required',true);

    }
    else {
        $("#div_id_dinhky").hide("slow");
        $("#id_dinhky").val('');
        $("#id_dinhky").prop('required',false);
    }
});




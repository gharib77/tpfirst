$('#add_more').click(function () {
    var form_idx = $('#id_form-TOTAL_FORMS').val();
    $('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
    $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
});
$('.del_btn').click(function () {
    $(item).css('display', 'none');
    ItemDelCheckbox.prop('checked', true);
});

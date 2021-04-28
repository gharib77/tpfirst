function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+-)');
    var replacement = prefix + '-' + ndx + '-';
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex,
    replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function addForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (formCount < 1000) {
        // Clone a form (without event handlers) from the first form
        var row = $(".item:last").clone(false).get(0);

        // Insert it after the last form
       $(row).removeAttr('id').hide().insertAfter(".item:last").slideDown(300);

        // Remove the bits we don't want in the new row/form
        // e.g. error messages
        $(".errorlist", row).remove();
        $(row).children().removeClass("error");

        // Relabel or rename all the relevant bits
    // Relabel/rename all the relevant bits
    $(row).children().children().each(function () {
      updateElementIndex(this, prefix, formCount);
      if ($(this).attr('type') == 'text')
        $(this).val('');
    });
        $(row).find('input:hidden').each(function () {
            updateElementIndex(this, prefix, formCount);
            $(this).val('');
            $(this).removeAttr('value');
            $(this).prop('checked', false);

        });

        // Add an event handler for the delete item/form link
        $(row).find(".delete").click(function () {
            return deleteForm(this, prefix);
        });
        // Update the total form count
        $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);

    } // End if

    return false;
}


function deleteForm(btn, prefix) {
  var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
  if (formCount > 1) {
    // Delete the item/form
    $(btn).parents('.item').remove();
    var forms = $('.item'); // Get all the forms
    // Update the total number of forms (1 less than before)
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
    var i = 0;
    // Go through the forms and set their indices, names and IDs
    for (formCount = forms.length; i < formCount; i++) {
      $(forms.get(i)).children().children().each(function () {
        updateElementIndex(this, prefix, i);
      });
    }


    }
      // End if

      return false;
  }
  var allids = [];
  $("body").on('click', '.remove-form-row',function () {
    var valinputtd = $(this).closest('tr').find('input:hidden').val()
    allids.push(valinputtd);
    $("input[name=recordelete]").val(allids);
      //$("#test").val(valinputtd)
      //console.log("hhhhhhhhhhh")
      deleteForm($(this), String($('.add-form-row').attr('id')));
  });

  $("body").on('click', '.add-form-row',function () {
      return addForm($(this), String($(this).attr('id')));
  });
  /*$(".add-form-row").click(function(){
    alert("jjjjjjjjj")
  })*/

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
  // You can only submit a maximum of 10 todo items 
  if (formCount < 10) {
    // Clone a form (without event handlers) from the first form
    var row = $(".item:first").clone(false).get(0);
    // Insert it after the last form
    $(row).removeAttr('id').hide().insertAfter(".item:last").slideDown(300);

    // Remove the bits we don't want in the new row/form
    // e.g. error messages
    $(".errorlist", row).remove();
    $(row).children().removeClass('error');

    // Relabel/rename all the relevant bits
    $(row).children().children().each(function () {
      updateElementIndex(this, prefix, formCount);
      if ($(this).attr('type') == 'text')
        $(this).val('');
    });

    // Add an event handler for the delete item/form link 
    $(row).find('.delete').click(function () {
      return deleteForm(this, prefix);
    });

    // Update the total form count
    $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);

  } // End if
  else {
    alert("Desculpe, mas você só pode adicionar um numero máximo de itens.");
  }
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

  } // End if
  else {
    alert("Você tem que entrar com pelo menos um item!");
  }
  return false;
}



var allids = [];

  $("body").on('click', '.remove-form-row',function () {
		var valinputtd= $(this).closest('tr').find('input:hidden').val()
		allids.push(valinputtd);
    $("input[name=recordelete]").val(allids);

	 // 
	  //alert(allids.length)
       //alert($("#test").val())
      deleteForm($(this), String($('.add-form-row').attr('id')));
  });

  $("body").on('click', '.add-form-row',function () {
      return addForm($(this), String($(this).attr('id')));
  });

// hier AJAX
$('#search-input').on('keyup', function(){
    var value = $(this).val()
    console.log('Suchwert:', value)
    })


//personen/person müssen reingeladen werden  personen = models.Person.objects.order_by

// var personen = '{{ personen|escapejs }}'

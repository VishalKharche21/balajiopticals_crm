
  
  $(document).ready(function () {

    // var count = 0;

    // $(document).on('click', '#add', function () {
    //   count++;
    //   var html = '';
    //   html += '<tr class="text-center">';
    //   html += '<td>' + count + '</td>';
    //   html += '<td><select name="product_id' + count + '" class="form-control item_category" data-sub_category_id="' + count + '"><option value="" selected disabled> Select Product Type</option><option value="Frame">Frame</option><option value="Glass">Glass</option><option value="Goggles">Goggles</option><option value="Contact Lens">Contact Lens</option><option value="Solution">Solution</option></select></td>';
    //   html += '<td><input type="text" name="modelname' + count + '" class="form-control" /></td>'
    //   html += '<td><input type="number" name="quantity' + count + '" class="form-control" /></td>'
    //   html += '<td><input type="number" name="purchase' + count + '" id="purchase' + count + '" class="form-control" /></td>'
    //   html += '<td><input type="number" name="tpurchase' + count + '" class="form-control" disabled style="background-color:rgb(255, 251, 235) ;" /></td>'
    //   html += '<td><button type="button" id="remove' + count + '" class="btn btn-secondary btn-sm remove mx-3">-</button></td>'
    //   $('.abcd').append(html);
    //   $("#totallength").val(count + 1);
    // });

    // $(document).on('click', ".remove", function () {
    //   $(this).closest('tr').remove();
    // });

    $(document).on('change', '.item_category', function () {
      var product_id = $(this).val();
      if (product_id == 'Frame' | product_id == 'Frame2' ) {
        // purchase 1
        new Autocomplete('#autocomplete', {
          search: input => {
            const url = `/autocomplete/?product_code=${input}`
            return new Promise(resolve => {
              fetch(url)
                .then(Response => Response.json())
                .then(data => {
                  resolve(data.data)
                });
            });
          }
        });
        // purchase 2
        new Autocomplete('#autocomplete1', {
          search: input => {
            const url = `/autocomplete/?product_code=${input}`
            return new Promise(resolve => {
              fetch(url)
                .then(Response => Response.json())
                .then(data => {
                  resolve(data.data)
                });
            });
          }
        });


      }
      else if (product_id == 'Glass') {

      }
      else if (product_id == 'Goggles') {

      }
      else if (product_id == 'Contact Lens') {

      }
      else if (product_id == 'Solution') {

      }
    });

    $(document).on('change', '.item_category', function () {
      var name = $(this).val()
      // purchase f1
      if (name == 'Frame') {
        $(document).on('change', '#framecodeid1', function () {
          var data = $('#framecodeid1').val().toLowerCase()
          var data1 = data.slice(0, 4)
          alert(data1)
          console.log(data1);
          $.ajax({
            url: "{% url 'purchaseajax' %}",
            data: { 'i': data1 },
            success: function (data) {
              $('#purchaseid1').val(data.d2)
            }
          });

        });
      }
      // purchase f2
      if (name == 'Frame2') {
        $(document).on('change', '#framecodeid2', function () {
          var data = $('#framecodeid2').val().toLowerCase()
          var data1 = data.slice(0, 4)
          console.log(data1);
          $.ajax({
            url: "{% url 'purchaseajax' %}",
            data: { 'i': data1 },
            success: function (data) {
              $('#purchaseid2').val(data.d2)
            }
          });

        });
      }
    });

    // purchase 1
    $(document).on('keyup', '#quantityid1', function () {
      const quantity = $('#quantityid1').val()
      const purchase = $('#purchaseid1').val()
      const total = parseFloat(quantity) * parseFloat(purchase)
      $('#tpurchaseid1').val(total);
      $('#tprsid').val(total);

    });
    // purchase 2
    $(document).on('keyup', '#quantityid2', function () {
      const quantity = $('#quantityid2').val()
      const purchase = $('#purchaseid2').val()
      const tp1 = $('#tpurchaseid1').val();
      const subtotal = parseFloat(quantity) * parseFloat(purchase)
      const total = parseFloat(subtotal) + parseFloat(tp1)
      $('#tpurchaseid2').val(subtotal);
      $('#tprsid').val(total);

    });
  });

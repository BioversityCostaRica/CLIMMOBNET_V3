/**
 * Created by lluis on 02/11/16.
 */

$('#hero-donut').each(function() {

    var x ="[['Hombres', 25],['Mujeres', 50]]";
    var data=[];
    x=x.split('],[');
    for (i =0; i<=x.length-1; i++){
        d=x[i].replace('[[', '').replace(']]', '').split(',')
        data.push({label: d[0], value: d[1] })

    }
    /*data=[
        {label: 'Maiz', value: 15 },
        {label: 'Fertilizantes', value: 14 },
        {label: 'Cacao', value: 10 },
        {label: 'Frijol', value: 8 },
        {label: 'Vainica', value: 8 },
        {label: 'Tomate', value: 24 },
        {label: 'as', value: 11 },
        {label: 'cafe', value: 10 },

    ];
    alert(data);*/

  Morris.Donut({
    element: 'hero-donut',
    data: data,
      //colors: ['#41cac0', '#49e2d7', '#34a39b'],
    colors: ['#eeae30', '#d69c2b', '#be8b26'],
    formatter: function (y) { return y + "%" }
  });


});



/**
 * Created by lluis on 02/11/16.
 */

$('.graph').each(function() {


  Morris.Donut({
    element: 'hero-donut',
    data: [
        {label: 'Maiz', value: 15 },
        {label: 'Fertilizantes', value: 14 },
        {label: 'Cacao', value: 10 },
        {label: 'Frijol', value: 8 },
        {label: 'Vainica', value: 8 },
        {label: 'Tomate', value: 24 },
        {label: 'as', value: 11 },
        {label: 'cafe', value: 10 },

    ],
      //colors: ['#41cac0', '#49e2d7', '#34a39b'],
    colors: ['#eeae30', '#d69c2b', '#be8b26'],
    formatter: function (y) { return y + "%" }
  });


});



$(function () {
    //Widgets count
    $('.count-to').countTo();


    initDonutChart("chart1");
    initBar("chart2");
    initAreaChart("chart3");
    initLineChart("chart4");


});

function initLineChart(element_id){

  Morris.Line({
  element: element_id,
  data: [
    { y: '2006', a: 100, b: 90 },
    { y: '2007', a: 75,  b: 65 },
    { y: '2008', a: 50,  b: 40 },
    { y: '2009', a: 75,  b: 65 },
    { y: '2010', a: 50,  b: 40 },
    { y: '2011', a: 75,  b: 65 },
    { y: '2012', a: 100, b: 90 }
  ],
  xkey: 'y',
  ykeys: ['a', 'b'],
  labels: ['Series A', 'Series B'],
  lineColors: ['#C72C41', '#801336', '#F9A26C', '#765D69', '#2D142C'],
  pointFillColors: ['#C72C41', '#801336', '#F9A26C', '#765D69', '#2D142C'],


});

}


function initAreaChart(element_id) {
    Morris.Area({
  element: element_id,
  data: [
    { y: '2006', a: 100, b: 90 },
    { y: '2007', a: 75,  b: 65 },
    { y: '2008', a: 50,  b: 40 },
    { y: '2009', a: 75,  b: 65 },
    { y: '2010', a: 50,  b: 40 },
    { y: '2011', a: 75,  b: 65 },
    { y: '2012', a: 100, b: 90 }
  ],
  xkey: 'y',
  ykeys: ['a', 'b'],
  labels: ['Series A', 'Series B'],
  pointFillColors: ['#C72C41', '#801336', '#F9A26C', '#765D69', '#2D142C'],
  lineColors: ['#C72C41', '#801336', '#F9A26C', '#765D69', '#2D142C'],
});
}

function initBar(element_id) {
    Morris.Bar({
            element: element_id,
            data: [{
                x: '2011 Q1',
                y: 3,
                z: 2,
                a: 3
            }, {
                    x: '2011 Q2',
                    y: 2,
                    z: null,
                    a: 1
                }, {
                    x: '2011 Q3',
                    y: 0,
                    z: 2,
                    a: 4
                }, {
                    x: '2011 Q4',
                    y: 2,
                    z: 4,
                    a: 3
                }],
            xkey: 'x',
            ykeys: ['y', 'z', 'a'],
            labels: ['Y', 'Z', 'A'],
            barColors: ['#C72C41', '#801336', '#F9A26C', '#765D69', '#2D142C'],
        });
}





function initDonutChart(element_id) {
    Morris.Donut({
        element: element_id,
        data: [{
            label: 'sajin',
            value: 37
        }, {
            label: '2',
            value: 30
        }, {
            label: '3',
            value: 18
        }, {
            label: '4',
            value: 12
        },
        {
            label: '5',
            value: 3
        }],
        colors: ['#C72C41', '#801336', '#F9A26C', '#765D69', '#2D142C'],
        formatter: function (y) {
            return y + '%'
        }
    });
}

var data = [], totalPoints = 110;
function getRandomData() {
    if (data.length > 0) data = data.slice(1);

    while (data.length < totalPoints) {
        var prev = data.length > 0 ? data[data.length - 1] : 50, y = prev + Math.random() * 10 - 5;
        if (y < 0) { y = 0; } else if (y > 100) { y = 100; }

        data.push(y);
    }

    var res = [];
    for (var i = 0; i < data.length; ++i) {
        res.push([i, data[i]]);
    }

    return res;
}


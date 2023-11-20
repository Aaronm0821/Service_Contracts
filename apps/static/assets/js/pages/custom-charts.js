'use strict';
$(document).ready(function() {
    setTimeout(function() {

        if (chartInfo['type'] == "Bar") {

            Morris.Bar({
                element: chartInfo['id'],
                data: chartData,
                xkey: chartInfo['xkey'],
                stacked: chartInfo['stack'],
                barSizeRatio: 0.70,
                barGap: 3,
                resize: true,
                responsive:true,
                ykeys: chartInfo['ykeys'],
                labels: chartInfo['labels'],
                barColors: chartInfo['barColors']
            });

        } else if (chartInfo['type'] == "Area") {

            Morris.Area({
                element: chartInfo['id'],
                data: chartData,
                lineColors: chartInfo['lineColors'],
                xkey: chartInfo['xkey'],
                ykeys: chartInfo['ykeys'],
                labels: chartInfo['labels'],
                pointSize: 0,
                lineWidth: 0,
                resize: true,
                fillOpacity: 0.8,
                responsive:true,
                behaveLikeLine: true,
                gridLineColor: '#e0e0e0',
                hideHover: 'auto',
                pointStrokeColors: chartInfo['pointStrokeColors'],
                smooth: chartInfo['smooth'],
            });

        } else if (chartInfo['type'] == "Line") {

            Morris.Line({
                element: chartInfo['id'],
                data: chartData,
                xkey: chartInfo['xkey'],
                ykeys: chartInfo['ykeys'],
                labels: chartInfo['labels'],
                lineColors: chartInfo['lineColors'],
                redraw: true,
                resize: true,
                responsive:true,
                hideHover: 'auto',
                smooth: chartInfo['smooth'],
            });

        } else if (chartInfo['type'] == "Donut") {

            var graph = Morris.Donut({
                element: chartInfo['id'],
                data: chartData,
                colors: [
                    '#1de9b6',
                    '#A389D4',
                    '#04a9f5',
                    '#1dc4e9',
                ],
                resize: true,
                formatter: chartInfo['formatter']
            });
        }
    }, 700);
});

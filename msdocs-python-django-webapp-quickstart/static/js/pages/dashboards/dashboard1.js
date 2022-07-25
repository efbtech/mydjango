// -------------------------------------------------------------------------------------------------------------------------------------------
// Dashboard 1 : Chart Init Js
// -------------------------------------------------------------------------------------------------------------------------------------------
$(function () {
    "use strict";
    // -----------------------------------------------------------------------
    // Sales of the Month
    // -----------------------------------------------------------------------
    appLoad();
var option_Sales_of_the_Month = {
        series: [9, 3, 2, 2],
        labels: ["Item A", "Item B", "Item C", "Item D"],
        chart: {
            type: 'donut',
            height: 280,
            fontFamily: 'Rubik,sans-serif',
        },
        dataLabels: {
            enabled: false,
        },
        stroke: {
            width: 0,
        },
        plotOptions: {
            pie: {
                expandOnClick: true,
                donut: {
                    size: '88',
                    labels: {
                        show: false,
                        name: {
                            show: true,
                            offsetY: 7,

                        },
                        value: {
                            show: false,
                        },
                        total: {
                            show: false,
                            color: '#a1aab2',
                            fontSize: '13px',
                            label: 'Our Visitor',
                        }
                    },
                },
            },
        },
        colors: ['#edf1f5', '#009efb', '#55ce63', '#745af2'],
        tooltip: {
            show: true,
            fillSeriesColor: false,
        },
        legend: {
            show: false
        },
    };

    var chart_pie_donut = new ApexCharts(document.querySelector("#sales-of-the-month"), option_Sales_of_the_Month);
    chart_pie_donut.render();

// -----------------------------------------------------------------------
// Revenue Statistics
// -----------------------------------------------------------------------

    var Revenue_Statistics = {
        series: [
            {
                name: "Product A ",
                data: [0, 2, 3.5, 0, 13, 1, 4, 1],
            },
            {
                name: "Product B ",
                data: [0, 4, 0, 4, 0, 4, 0, 4],
            },
        ],
        chart: {
            fontFamily: 'Rubik,sans-serif',
            height: 350,
            type: "area",
            toolbar: {
                show: false,
            },
        },
        fill: {
            type: 'solid',
            opacity: 0.2,
            colors: ["#009efb", "#39c449"],
        },
        grid: {
            show: true,
            borderColor: "rgba(0,0,0,0.1)",
            strokeDashArray: 3,
            xaxis: {
                lines: {
                    show: true
                }
            },  
        },
        colors: ["#39c449", "#009efb"],
        dataLabels: {
            enabled: false,
        },
        stroke: {
            curve: "smooth",
            width: 1,
            colors: ["#009efb", "#39c449"],
        },
        markers: {
            size: 3,
            colors: ["#009efb", "#39c449"],
            strokeColors: "transparent",
        },
        xaxis: {
            axisBorder: {
                show: true,
            },
            axisTicks: {
                show: true,
            },
            categories: ['0', '4', '8', '12', '16', '20', '24', '30'],
            labels: {
                style: {
                    colors: "#a1aab2",
                },
            },
        },
        yaxis: {
            tickAmount: 9,
            labels: {
                style: {
                    colors: "#a1aab2",
                },
            },
        },
        tooltip: {
            x: {
                format: "dd/MM/yy HH:mm",
            },
            theme: "dark",
        },
        legend: {
            show: false,
        },
    };

    var chart_area_spline = new ApexCharts(document.querySelector("#revenue-statistics"), Revenue_Statistics);
    chart_area_spline.render();
    
// ----------------------------------------------------------------------- 
// Sales difference
// -----------------------------------------------------------------------

var option_Sales_Difference = {
        series: [35, 15, 10],
        labels: ["", "", ""],
        chart: {
            type: 'donut',
            height: 140,
            fontFamily: 'Rubik,sans-serif',
        },
        dataLabels: {
            enabled: false,
        },
        stroke: {
            width: 0,
        },

        plotOptions: {
            pie: {
                expandOnClick: true,
                donut: {
                    size: '65%',
                    labels: {
                        show: false,
                        name: {
                            show: true,
                            offsetY: 7,

                        },
                        value: {
                            show: false,
                        },
                        total: {
                            show: false,
                            color: '#a1aab2',
                            fontSize: '13px',
                            label: 'Visits',
                        }
                    },
                },
            },
        },
        colors: ['#39c449',  '#ebf3f5', '#009efb'],
        tooltip: {
            show: true,
            fillSeriesColor: false,
        },
        legend: {
            show: false
        },
        responsive: [{
            breakpoint: 426,
            options: {
                chart: {
                    height: 130,
                    offsetY: 10,
                    offsetX: -35,
                    width: 200
                },
            }
        }]
    };

    var chart_pie_donut = new ApexCharts(document.querySelector("#sales-difference"), option_Sales_Difference);
    chart_pie_donut.render(); 


// ----------------------------------------------------------------------- 
// Sales Prediction
// ----------------------------------------------------------------------- 


var option_Sales_Prediction = {
        chart: {
            height: 170,
            type: "radialBar",
            fontFamily: 'Rubik,sans-serif',
            spacingTop: 0,
            spacingBottom: 0,
            spacingLeft: 0,
            spacingRight: 0,
            offsetY: -30,
            sparkline: {
                enabled: true
            }
        },
        series: [60],
        colors: ["#1badcb"],
        stroke: {
          dashArray: 2
        },
        plotOptions: {
            radialBar: {
                startAngle: -135,
                endAngle: 135,
                track: {
                    background: '#f1f1f1',
                    startAngle: -135,
                    endAngle: 135,
                },
                hollow: {
                    size: '30%',
                    background: 'transparent',
                },
                dataLabels: {
                    show: true,
                    name: {
                        show: false,
                    },
                    value: {
                        show: false,
                    },
                    total: {
                      show: true,
                      fontSize: '20px',
                      color: '#000', 
                      label: '91.4 %', 
                  }
                }
            }
        },
        fill: {
            type: "solid",
        },
        tooltip: {
          enabled: true, 
          fillSeriesColor: false,
          theme: "dark"
        },
        responsive: [{
            breakpoint: 426,
            options: {
                chart: {
                    offsetX: -15,
                }
            }
        }],
        labels: ["Progress"]
    };

    new ApexCharts(document.querySelector("#sales-prediction"), option_Sales_Prediction).render();
});

$(document).on({
    ajaxStart: function(){
        $("body").addClass("loading"); 
    },
    ajaxStop: function(){ 
        $("body").removeClass("loading"); 
    }    
});

function appLoad() {
    $('input[type=radio][name=debtorlist]').change(function(){
        if(this.value == 1) {
            $('#nid').css('display','none');
            $('#idn').css('display','block');
        }
        if(this.value == 2) {
            $('#idn').css('display','none');
            $('#nid').css('display','block');
        }
    });

    $('#curram').change(function(){
        if(this.value == 'Curr Amt') {
            var checkedVals = $('input:checkbox[name=trans]:checked').map(function() {
                return $(this).data('ca');
            }).get();
        }
        if(this.value == 'Ex GST') {
            var checkedVals = $('input:checkbox[name=trans]:checked').map(function() {
                return $(this).data('eg');
            }).get();
        }
        if(this.value == 'Inc GST') {
            var checkedVals = $('input:checkbox[name=trans]:checked').map(function() {
                return $(this).data('ig');
            }).get();
        }
        var tot = checkedVals.reduce((a, b) => parseFloat(a) + parseFloat(b), 0);
        $('#agingsummary45').text(setdecimal(tot));
    });

    //checkbox code here

    $('input[type=radio][name=transaction_status]').change(function(){
        $('#exp_trans').val(this.value)
        if(this.value == 'history') {
            $('#transdata').addClass('bg-info');
        } else {
            $('#transdata').removeClass('bg-info');
        }
        $.ajax({url: "/ajaxreq/", data:{type:'transtype',trans:this.value,debtor:$('#idn').val()}, success: function(result){
            trans = '';
            $(result.data.transaction_list).each(function(ix,v) {
                trans += '<tr><td class="text-nowrap"><input type="checkbox" name="trans"></td><td class="text-nowrap">'+v[0]+'</td><td class="text-nowrap">'+v[1]+'</td><td class="text-nowrap">'+v[2]+'</td><td class="text-nowrap">'+v[3]+'</td><td class="text-nowrap">'+v[4]+'</td><td class="text-nowrap">'+v[5]+'</td><td class="text-nowrap">'+v[6]+'</td><td class="text-nowrap">'+v[7]+'</td><td class="text-nowrap">'+v[8]+'</td><td class="text-nowrap">'+v[9]+'</td><td class="text-nowrap">'+v[10]+'</td><td class="text-nowrap">'+v[11]+'</td><td class="text-nowrap">'+v[12]+'</td></tr>';
            });
            $('#transdata').html(trans);
        }});
    });

    $('select#idn').change(function(){
        setdebtor(this.value);
    })
    $('select#nid').change(function(){
        setdebtor(this.value);
    })
}

function filterage(aging){
    $.ajax({url: "/ajaxreq/", data:{type:'transtype',trans:aging,debtor:$('#idn').val()}, success: function(result){
        trans = '';
        $(result.data.transaction_list).each(function(ix,v) {
            trans += '<tr><td class="text-nowrap"><input type="checkbox" name="trans"></td><td class="text-nowrap">'+v[0]+'</td><td class="text-nowrap">'+v[1]+'</td><td class="text-nowrap">'+v[2]+'</td><td class="text-nowrap">'+v[3]+'</td><td class="text-nowrap">'+v[4]+'</td><td class="text-nowrap">'+v[5]+'</td><td class="text-nowrap">'+v[6]+'</td><td class="text-nowrap">'+v[7]+'</td><td class="text-nowrap">'+v[8]+'</td><td class="text-nowrap">'+v[9]+'</td><td class="text-nowrap">'+v[10]+'</td><td class="text-nowrap">'+v[11]+'</td><td class="text-nowrap">'+v[12]+'</td></tr>';
        });
        $('#transdata').html(trans);
    }});
}

function transaction_check(){
    $('input:checkbox[name=trans]').change(function() {
        if($('#curram').val() == 'Curr Amt') {
            var checkedVals = $('input:checkbox[name=trans]:checked').map(function() {
                return $(this).data('ca');
            }).get();
        }
        if($('#curram').val() == 'Ex GST') {
            var checkedVals = $('input:checkbox[name=trans]:checked').map(function() {
                return $(this).data('eg');
            }).get();
        }
        if($('#curram').val() == 'Inc GST') {
            var checkedVals = $('input:checkbox[name=trans]:checked').map(function() {
                return $(this).data('ig');
            }).get();
        }
        var tot = checkedVals.reduce((a, b) => parseFloat(a) + parseFloat(b), 0);
        $('#agingsummary45').text(Math.round( tot * 100 + Number.EPSILON ) / 100);
    });

    //supplier

    $('input:checkbox[name=filterx]').change(function() {
        var checkedVals = $('input:checkbox[name=filterx]:checked').map(function() {
            return this.value;
        }).get();
        //$('#transdata tr').removeClass('d-none');
        $('#transdata tr').addClass('d-none');
        var expfilters = '';
        jQuery.each(checkedVals, function(index, item) {
            console.log(item);
            expfilters += '<input type="hidden" name="expfil[]" value="'+item+'">';
            //$('#mfilters').
            if(item.startsWith("[")){
                if(item == '[Exclude $0.00]') {
                    var checkedGrid = $('input:checkbox[name=trans]').map(function() {
                        if($(this).data('ca')!=0) {
                            $(this).parent().parent().removeClass('d-none');
                        }
                    }).get();
                }
                if(item == '[Load Overdue]') {
                    var checkedGrid = $('input:checkbox[name=trans]').map(function() {
                        if($(this).data('overdue') > 0) {
                            $(this).parent().parent().removeClass('d-none');
                        }
                    }).get();
                }
                if(item == '[Load Invoices]') {
                    var checkedGrid = $('input:checkbox[name=trans]').map(function() {
                        if($(this).data('doctype')=='Invoice') {
                            $(this).parent().parent().removeClass('d-none');
                        }
                    }).get();
                }
                if(item == '[Load Credits/Payments]') {
                    var checkedGrid = $('input:checkbox[name=trans]').map(function() {
                        if($(this).data('doctype')=='Credit') {
                            $(this).parent().parent().removeClass('d-none');
                        } if($(this).data('doctype')=='Payment') {
                            $(this).parent().parent().removeClass('d-none');
                        }
                    }).get();
                }
            } else {
                var checkedGrid = $('input:checkbox[name=trans]').map(function() {
                    if($(this).data('supplier')==item) {
                        $(this).parent().parent().removeClass('d-none');
                    }
                }).get();
            }
            
        });
        $('#mfilters').html(expfilters)
    });
}

function setdecimal(tot) {
    return Math.round( tot * 100 + Number.EPSILON ) / 100
}

function reqcopy() {
    if($('#idn').val() == '') {
        alert('Select a valid member to proceed further')
        return true
    }
    if($("#transdata input:checkbox:checked").length == 0){
        alert('No selection to proceed further')
        return true
    }
    var trlist = [];
    var a = '';
    var b= '';
        $("table > tbody#transdata > tr").each(function () {
            var tdlist = [];

            /*textlist = $(this).find("input:checkbox[name=trans]:checked").map( function(){
                return $(this).find('td').text();        
            }).get().join('++++');*/
            if ($(this).find("td input:checkbox[name=trans]").is(":checked")) {
                console.log('check')
                tdlist.push($(this).find("td input:checkbox[name=trans]:checked").data('supplier'));
                tdlist.push($(this).find('td').eq(1).text());
                /*tdlist.push($(this).find('td').eq(2).text());
                tdlist.push($(this).find('td').eq(3).text());
                tdlist.push($(this).find('td').eq(4).text());
                tdlist.push($(this).find('td').eq(5).text());
                tdlist.push($(this).find('td').eq(6).text());
                tdlist.push($(this).find('td').eq(7).text());
                tdlist.push($(this).find('td').eq(8).text());
                tdlist.push($(this).find('td').eq(9).text());
                tdlist.push($(this).find('td').eq(10).text());
                tdlist.push($(this).find('td').eq(11).text());
                tdlist.push($(this).find('td').eq(12).text());
                tdlist.push($(this).find('td').eq(13).text());
                tdlist.push($(this).find('td').eq(14).text());*/
                var z = tdlist.join('++++');
                trlist.push(z);
                //console.log($(this).find('td').eq(1).text() + " " + $(this).find('td').eq(2).text());
            }
            
            
                
            
        });
        var trl = trlist.join('___');
        //trlx
        console.log('Starting')
        var fr = new Array();
        jQuery.each(trlist, function(index, item) {
            itx = item.split('++++')
            fr[itx[0]].push(itx[1])
            //console.log(index+'---'+item)
        });
        console.log(fr);
        //console.log(trlist.join('___'));
    /*textlist = $("span.gtx").map( function(){
        return $(this).text();        
    }).get().join('++++');
    console.log(textlist)*/
    $.ajax({url: "/ajaxreq/", data:{info:$('#idn').val(), memname:$('select#idn option:selected').text(), chdata:$("#transdata input:checkbox:checked").data('supplier'), type:'requestcopy', sopt:trl}, success: function(result){
        
    }});
}

function overduemail() {
    if($('#idn').val() == '') {
        alert('Select a valid member to proceed further')
        return true
    }
    if($("#transdata input:checkbox:checked").length == 0){
        alert('No selection to proceed further')
        return true
    }
    $('input:checkbox[name=trans]:checked').map(function() {
        if($(this).data('overdue') == 'null' || $(this).data('overdue') == 0) {
            alert('No overdue days');
            return true
        }
    });
    
    var trlist = [];
    var a = '';
    var b= '';
        $("table > tbody#transdata > tr").each(function () {
            var tdlist = [];

            /*textlist = $(this).find("input:checkbox[name=trans]:checked").map( function(){
                return $(this).find('td').text();        
            }).get().join('++++');*/
            if ($(this).find("td input:checkbox[name=trans]").is(":checked")) {
                console.log('check')
                tdlist.push($(this).find('td').eq(1).text());
                tdlist.push($(this).find('td').eq(2).text());
                tdlist.push($(this).find('td').eq(4).text());
                tdlist.push($(this).find('td').eq(5).text());
                tdlist.push($(this).find('td').eq(6).text());
                tdlist.push($(this).find('td').eq(7).text());
                tdlist.push($(this).find('td').eq(8).text());
                tdlist.push($(this).find('td').eq(9).text());
                tdlist.push($(this).find('td').eq(10).text());
                tdlist.push($(this).find('td').eq(11).text());
                tdlist.push($(this).find('td').eq(12).text());
                tdlist.push($(this).find('td').eq(14).text());
                tdlist.push($(this).find('td').eq(15).text());
                var z = tdlist.join('++++');
                trlist.push(z);
                //console.log($(this).find('td').eq(1).text() + " " + $(this).find('td').eq(2).text());
            }
            
            
                
            
        });
        //var trl = trlist.join('___');
        trlx = trl.split()
        console.log('Starting')
        jQuery.each(trlx, function(index, item) {
            console.log(index+'---'+item)
        });
        //console.log(trlist.join('___'));
    /*textlist = $("span.gtx").map( function(){
        return $(this).text();        
    }).get().join('++++');
    console.log(textlist)*/
    $.ajax({url: "/ajaxreq/", data:{info:$('#idn').val(), memname:$('select#idn option:selected').text(), chdata:$("#transdata input:checkbox:checked").data('supplier'), type:'overdue', sopt:trl}, success: function(result){

    }});
}

function setdebtor(a) {
    $.ajax({url: "/ajaxreq/", data:{info:$('#idn').val(),type:'setdebtor'}, success: function(result){
        if(result.success) {
            $('#exp_debtor').val(a);
            $(result.data.memberdetail).each(function(index,elem) {
                $('#memd1').text(elem[1])
                $('#memd17').text(elem[17])
                $('#memd20').text(elem[20])
                if(elem[6] === true) {
                    $('#memd6').text('On Hold')
                } else {
                    $('#memd6').text('Off Hold')
                }
                $('#agingsummaryo04').text(setdecimal(elem[22]))
                $('#agingsummary40').text(setdecimal(elem[49])+' / '+setdecimal(elem[50]))
            });
            $(result.data.agingsummary).each(function(index,elem) {
                $('#agingsummary3').html('<a href="#" onclick="filterage(\'CURR\')">'+setdecimal(elem[3])+'</a>')
                $('#agingsummary4').html('<a href="#" onclick="filterage(\'1to30\')">'+setdecimal(elem[4])+'</a>')
                $('#agingsummary5').html('<a href="#" onclick="filterage(\'31to60\')">'+setdecimal(elem[5])+'</a>')
                $('#agingsummary6').html('<a href="#" onclick="filterage(\'61to90\')">'+setdecimal(elem[6])+'</a>')
                $('#agingsummary7').html('<a href="#" onclick="filterage(\'90Plus\')">'+setdecimal(elem[7])+'</a>')
                $('#agingsummary0').html('<a href="#" onclick="filterage(\'ALL\')">'+setdecimal(parseFloat(elem[4])+parseFloat(elem[5])+parseFloat(elem[6]) + parseFloat(elem[7]))+'</a>')

                $('#agingsummaryo0').html('<a href="#" onclick="filterage(\'DueEOM\')">'+setdecimal(elem[0])+'</a>')
                $('#agingsummaryo1').html('<a href="#" onclick="filterage(\'DueEONM\')">'+setdecimal(elem[1])+'</a>')
                $('#agingsummaryo2').html('<a href="#" onclick="filterage(\'DueEOFM\')">'+setdecimal(elem[2])+'</a>')
                $('#agingsummaryo03').text(setdecimal(elem[0]))
                var ocv = parseFloat(result.data.memberdetail[0][22]) - (parseFloat(elem[4])+parseFloat(elem[5])+parseFloat(elem[6]) + parseFloat(elem[7]));
                $('#agingsummaryo05').text(setdecimal(ocv))
                
            });

            $(result.data.latestdetail).each(function(index,elem) {
                $('#agingsummary41').text(setdecimal(elem[2]));
                let elem3date =new Date(elem[3]);
                let elem0date =new Date(elem[0]);
                $('#agingsummary42').text(elem3date.toLocaleDateString());
                $('#agingsummary43').text(elem0date.toLocaleDateString());
            });
            $('#agingsummary44').text(setdecimal(result.data.memberdetail[0][22]));

            vdrop = '';
            $(result.data.vaultdropdown).each(function(index,elem) {
                vdrop += '<option value="'+elem[1]+'">'+elem[0]+'</option>';
            });
            $('#curram').html(vdrop);
            $('#mfilters').html('');
            
            str = '';
            supp = '';
            trans = '';
            $(result.data.systemparam).each(function(index,elem) {
                str += '<div class="border-bottom p-2"><input type="checkbox" name="filterx" value="'+elem[0]+'"> '+elem[0]+'</div>';
            });

            $(result.data.supplier).each(function(index,elem) {
                supp += '<div class="border-bottom p-2"><input type="checkbox" name="filterx" value="'+elem[0]+'"> '+elem[2]+'</div>';
            });

            $(result.data.transaction_open).each(function(ix,v) {
                let elemxdate =new Date(v[14]);
                let v5date =new Date(v[5]);
                let v6date =new Date(v[6]);
                trans += '<tr><td class="text-nowrap"><input type="checkbox" value="'+v[11]+'_'+v[8]+'_'+v[10]+'" name="trans" data-supplier="'+v[3]+'" data-doctype="'+v[1]+'" data-overdue="'+v[7]+'" data-ca="'+v[11]+'" data-eg="'+v[8]+'" data-ig="'+v[10]+'"></td><td class="text-nowrap"><span class="gtx">'+v[0]+'</span></td><td class="text-nowrap"><span class="gtx">'+v[1]+'</span></td><td class="text-nowrap"><span class="gtx">'+v[2]+'</span></td><td class="text-nowrap"><span class="gtx">'+v[4]+'</span></td><td class="text-nowrap"><span class="gtx">'+v5date.toLocaleDateString()+'</span></td><td class="text-nowrap"><span class="gtx">'+v6date.toLocaleDateString()+'</span></td><td class="text-nowrap"><span class="gtx">'+setdecimal(v[7])+'</span></td><td class="text-nowrap"><span class="gtx">'+setdecimal(v[8])+'</span></td><td class="text-nowrap"><span class="gtx">'+setdecimal(v[9])+'</span></td><td class="text-nowrap"><span class="gtx">'+setdecimal(v[10])+'</span></td><td class="text-nowrap"><span class="gtx">'+setdecimal(v[11])+'</span></td><td class="text-nowrap"><span class="gtx">'+setdecimal(v[12])+'</span></td><td class="text-nowrap" class="x"><span class="gtx">'+elemxdate.toLocaleDateString()+'</span></td><td class="text-nowrap"><span class="gtx">'+v[15]+'</span></td></tr>';
            });

            $('#filterdata').html(str);
            $('#suppliersdata').html(supp);
            $('#transdata').html(trans);
            $('#memdetail').removeClass('d-none');
            $('#agingsummary').removeClass('d-none');
            $('#agingsummaryo').removeClass('d-none');

            transaction_check();

        }
    }});
    //location.href='/aging/?debtor='+a;
}


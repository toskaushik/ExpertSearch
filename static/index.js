var startResults = 5;
var numResults = startResults;
var incResults = 2;
var searchTerm = ''



var docDiv = (doc) => {
    const name = doc[0];
    const prev = doc[1];
    const fac_name = doc[2];
    const fac_url = doc[3];
    return (`<section class="col-xs-12 col-sm-6 col-md-12 mb-3">
                <article class="search-result row">
                    <div class="col-xs-12 col-sm-12 col-md-12 excerpet">
                     <h4 class = "mb-0 mt-0"  style="font-weight:bold"><a href=${fac_url} title="">${fac_name}</a></h4>
                      <p class = "mb-0 mt-0" style = "font-size:medium">${prev}</p>
                       <h7>${fac_url}</h7>
                    </div>
                    <span class="clearfix borda"></span>
                </article>
            </section>`
            );
}

var doSearch = function() {
    const data = {
        "query": searchTerm,
        "num_results": numResults
    }
    if (searchTerm!='')
    {
    var num_fetched_res = 0
    fetch("http://localhost:8095/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    }).then(response => {
        response.json().then(data => {
            const docs = data.docs;
            $("#docs-div").empty();
            $("#docs-div").append('<h4>Search Results For <q><strong class="text-danger">'+searchTerm+'</strong></q></h4> <br>');
            docs.forEach(doc => {

                $("#docs-div").append(
                    docDiv(doc)
                );
                    num_fetched_res = num_fetched_res+1;

            });
            if (num_fetched_res==numResults){

            $("#loadMoreButton").css("display", "block")
        }
        else{
            $("#loadMoreButton").css("display", "none")
        }
        if (num_fetched_res==0){
            $("#docs-div").append(`<h3 style="text-align: center;margin-top:20px;">No Search Results Found</h3>`);
        }
        })

    });
}
}

$(window).on("resize",function() {
    $(document.body).css("margin-top", $(".navbar").height()+5 );
    var width = $(".select2-container").width()
    if ((width == 0)||width===undefined){
        width = 300
    }
    $(".select2-search__field").css('cssText', $(".select2-search__field").attr('style')+'width: ' + width+ 'px !IMPORTANT;');
}
).resize();


$(document).ready(function() {
    $(window).trigger('resize');
});

window.onload=function(){
    $(window).trigger('resize');

};

function  toggleFilter() {
}

$("#submitButton").click(function() {
    numResults = startResults;
    searchTerm = $('#query').val()
    doSearch();
});

$('#query').keydown(function(e) {
    searchTerm = $('#query').val()
    if (e.keyCode == 13) {
        numResults = startResults;
    doSearch();
    }
});

$("#loadMoreButton").click(function() {
    numResults += incResults
    doSearch();
});
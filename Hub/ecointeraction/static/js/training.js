d3.json("data.json",function(treeData){
var margin = {top: 0, right: 155, bottom: 100, left:25},
    width = document.getElementById("div-tree").offsetWidth - margin.right - margin.left,
    height = document.getElementById("div-tree").offsetHeight- margin.top - margin.bottom;
    
var i = 0,
    duration = 800,
    /*delay_link_exit = 100,
    delay_link_enter = 25,*/
    delay_link_exit = 0,
    delay_link_enter = 0,
    root;
	
var padding = 0;
var padding_length=width;
// var link_length = 180;

var link_length = width;

var tree = d3.layout.tree()
    .size([height, width]);

var diagonal = d3.svg.diagonal()
    .projection(function(d) { return [d.y, d.x]; });

var svg = d3.select("#tree").append("svg")
    .attr("width", width + margin.right + margin.left)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

root = treeData;
root.x0 = height / 2;
root.y0 = 0;
$("#div-content").load('default.html');
update(root);

function update(source) {
  // Compute the new tree layout.
  var nodes = tree.nodes(root).reverse(),
      links = tree.links(nodes); 
  // Normalize for fixed-depth.
  if(source._children)padding-=source.y0;
  else if(source.children) padding+=padding_length-source.y0;
  nodes.forEach(function(d) {
	  d.y = width-((d.depth * link_length)-padding);
  });

  var node = svg.selectAll("g.node")
      .data(nodes, function(d) { return d.id || (d.id = ++i); });
      
  // Enter any new nodes at the parent's previous position.
  var nodeEnter = node.enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
      .on("click", click);

  nodeEnter.append("circle")
      .attr("r", 10)
      .style("fill", function(d) { return d._children ? "#0033CC" : "#0033CC"; });

  nodeEnter.append("text")
      /**.attr("x", function(d) { return d.children || d._children ? -30 : 30; })**/
      .attr("x", function(d) { return d.children || d._children ? +30 : +30; })
      .attr("dy", ".35em")
      /*.attr("text-anchor", function(d) { return d.children || d._children ? "end" : "start"; })*/
      .attr("text-anchor", function(d) { return d.children || d._children ? "start" : "start"; })
      .text(function(d) { return d.name; })
      .style("fill-opacity", 1e-6)
     .attr("class", function(d) {
              if (d.url != null) { return 'hyper'; } 
         })
          .on("click", function (d) { 
              $('.hyper').attr('style', 'font-weight:normal');
              d3.select(this).attr('style', 'font-weight:bold');
              if (d.url != null) {
                 //  window.location=d.url; 
                 $('#vid').remove();

                 $('#vid-container').append( $('<embed>')
                    .attr('id', 'vid')
                    .attr('src', d.url + "?version=3&amp;hl=en_US&amp;rel=0&amp;autohide=1&amp;autoplay=1")
                    .attr('wmode',"transparent")
                    .attr('type',"application/x-shockwave-flash")
                    .attr('width',"100%")
                    .attr('height',"100%") 
                    .attr('allowfullscreen',"true")
                    .attr('title',d.name)
                  )
                }
          }) 
    ;
  // Transition nodes to their new position.
  var nodeUpdate = node.transition()
      .duration(duration)
      .attr("transform", function(d) {return "translate(" + d.y+ "," + d.x+ ")"; });
	  
 /* if(source.children){
    nodeUpdate.select("circle")
        .transition()
        .duration(duration)
        .attr("r", 20)
        .style("fill", function(d) { return d._children ? "#0033CC" : "#ADD9E4"; })
        .each("end",_.once(goToContentWithDelay));
  }
  else if(!source._children) {
    nodeUpdate.select("circle")
        .attr("r", 20)
        .style("fill", function(d) { return d._children ? "#0033CC" : "#ADD9E4"; });
        goToContent();
  }
  else {
   nodeUpdate.select("circle")
      .transition()
      .duration(duration)
      .attr("r", 20)
      .style("fill", function(d) { return d._children ? "#0033CC" : "#ADD9E4"; }); 
  }*/
  
   nodeUpdate.select("circle")
      .transition()
      .duration(duration)
      .attr("r", 20)
      .style("fill", function(d) { return d._children ? "#0033CC" : "#ADD9E4"; });

  nodeUpdate.select("text")
      .transition()
      .duration(duration)
      .style("fill-opacity", 1);

  // Transition exiting nodes to the parent's new position.
  var nodeExit = node.exit()
      .transition()
      .duration(duration)
      .attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
      .remove();

  nodeExit.select("circle")
      .attr("r", 1e-6);


  nodeExit.select("text")
      .transition()
      .duration(duration)
      .style("fill-opacity", 1e-6);

  // Update the links…
  var link = svg.selectAll("path.link")
      .data(links, function(d) { return d.target.id; });

  // Enter any new links at the parent's previous position.
  link.enter().insert("path", "g")
      .attr("class", "link")
      .attr("d", function(d) {
        var o = {x: source.x0, y: source.y0};
        return diagonal({source: o, target: o});
      });

  // Transition links to their new position.
  link.transition()
      .duration(duration)
      .attr("d", diagonal);

  // Transition exiting nodes to the parent's new position.
  link.exit().transition()
      .duration(duration)
      .attr("d", function(d) {
        var o = {x: source.x, y: source.y};
        return diagonal({source: o, target: o});
      })
      .remove();

  // Stash the old positions for transition.
  nodes.forEach(function(d) {
    d.x0 = d.x;
    d.y0 = d.y;
  });
}

function removeChildren(d){
  if (d.children) {
    d.children.forEach(function(child){
      removeChildren(child);
    });
    d._children = d.children;
    d.children = null;
  }
}
// Toggle children on click.
function goToContentWithDelay(){
      $('html, body').delay(duration/2).animate({
        scrollTop: $("#div-content").offset().top
    }, duration);
}
function goToContent(){
      $('html, body').animate({
        scrollTop: $("#div-content").offset().top
    }, duration);
}
function click(d) {
  var html_file = 'default.html';

  if (d.children) {
    if(d.depth){
       html_file = encodeURI(d.parent.html);
    }
    removeChildren(d);
  } else {
    html_file = encodeURI(d.html);
    d.children = d._children;
    d._children = null;
  }
  $("#div-content").load(html_file);
  update(d);
}
	
});




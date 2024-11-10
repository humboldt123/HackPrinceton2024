window.addEventListener("load", () => graph());
async function graph() {
  let container = document.getElementById("roadmap");
  let options = await (await fetch("/scribble.json")).json();


  let connections = await (await fetch("/dummygraph.json")).json();

  let data = {nodes: [], edges: []};
  let links = new Set();

  // Loop through connections...
  for (el in connections) {
    item = connections[el];
      // Add to nodes
      data.nodes.push({
        id: el,//
        image: "",
        label: item.title,
      });
      // Add the links to our set
      // item.connections.forEach(mutual => links.add([id, mutual].sort((a, b) => parseInt(a) - parseInt(b)).join(" ")));
    
  }

  // Register each link in edges
  // [...links].forEach(link => data.edges.push({from:parseInt(link.split(" ")[0]), to:parseInt(link.split(" ")[1])}));

  network = new vis.Network(container, data, options);
}
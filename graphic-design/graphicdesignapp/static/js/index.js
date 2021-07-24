let designs;

function truncate(str, len) {
  if (str.length > len && str.length > 0) {
    let new_str = str + " ";
    new_str = str.substr(0, len);
    new_str = str.substr(0, new_str.lastIndexOf(" "));
    new_str = new_str.length > 0 ? new_str : str.substr(0, len);
    return new_str + "...";
  }
  return str;
}

async function listDesignsInUI(param) {
  try {
    designs = param;
    const DOMdesigns = document.getElementById("designs");
    designs.forEach((design) => {
      const col = document.createElement("div");
      col.classList.add("col-sm-12", "col-md-6", "col-lg-4", "mt-2");

      const card = document.createElement("div");
      card.classList.add("card");

      const a = document.createElement("a");
      a.href = `designs/${design.pk}`;

      const cardImage = document.createElement("img");
      cardImage.classList.add("card-image", "w-100");
      cardImage.height = 200;
      cardImage.src = design.fields.image;
      a.appendChild(cardImage);
      card.appendChild(a);

      const header = document.createElement("div");
      header.classList.add("card-header");

      const sellerData = document.createElement("span");
      sellerData.classList.add("seller-info");

      const sellerImageContainer = document.createElement("span");

      const sellerImage = document.createElement("img");
      sellerImage.classList.add("rounded-circle");
      sellerImage.height = 50;
      sellerImage.width = 50;
      sellerImage.src =
        "https://i.pinimg.com/736x/8b/16/7a/8b167af653c2399dd93b952a48740620.jpg";

      sellerImageContainer.appendChild(sellerImage);
      sellerData.appendChild(sellerImageContainer);

      const sellerInfo = document.createElement("span");
      sellerInfo.classList.add("mx-2");

      const sellerName = document.createElement("p");
      sellerName.classList.add("text-dark", "p-0", "m-0");
      sellerName.innerHTML = design.fields.name;

      const seller = document.createElement("p");
      seller.classList.add("text-muted", "p-0", "m-0");
      seller.innerHTML = "Seller";

      sellerInfo.appendChild(sellerName);
      sellerInfo.appendChild(seller);

      const category = document.createElement("span");
      category.classList.add("mt-3");
      category.innerHTML = `<b>Category: </b> ${design.fields.category}`;

      sellerData.appendChild(sellerInfo);
      header.appendChild(sellerData);
      header.appendChild(category);
      card.appendChild(header);

      const cardBody = document.createElement("div");
      cardBody.classList.add("card-body", "text-dark");
      cardBody.id = "desc";

      const desc = document.createElement("p");
      desc.classList.add("desc");
      desc.innerHTML = truncate(design.fields.description, 50);

      cardBody.appendChild(desc);
      card.appendChild(cardBody);

      const horizontalRule = document.createElement("hr");
      card.appendChild(horizontalRule);

      const price = document.createElement("p");
      price.classList.add("d-flex", "justify-content-end", "mx-2");
      price.innerHTML = `STARTING AT: &#x20AC; <span class="font-weight-bold">${design.fields.price}</span>`;

      card.appendChild(price);
      col.appendChild(card);
      DOMdesigns.appendChild(col);
    });
  } catch (err) {
    console.error(err.message);
    alert(err.message);
  }
}

function filterDesigns(e) {
  const text = document.getElementById("filtertext").value;
  if (text !== "") {
    const filteredDesigns = designs.filter((design) => {
      const regexp = new RegExp(`${text}`, "gi");
      return design.fields.category.match(regexp);
    });
    // Keep track of old Designs
    const oldDesigns = designs;
    removeChildNodes();
    listDesignsInUI(filteredDesigns);
    // Assign all Designs so that the filtering happens on all Designs every time the input is changed
    designs = oldDesigns;
  } else {
    removeChildNodes();
    axios
      .get("/accounts/designs/")
      .then((res) => listDesignsInUI(res.data))
      .catch((err) => {
        console.error(err.message);
      });
  }
}

function removeChildNodes() {
  const nodes = document.getElementById("designs");
  while (nodes.hasChildNodes()) {
    nodes.removeChild(nodes.firstChild);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  axios
    .get("/accounts/designs/")
    .then((res) => listDesignsInUI(res.data))
    .catch((err) => {
      console.error(err.message);
    });
});

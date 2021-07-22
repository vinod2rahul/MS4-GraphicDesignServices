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

async function getDesign() {
  try {
    const res = await axios.get("/accounts/designs/");
    const designs = res.data;
    const DOMdesigns = document.getElementById("designs");
    designs.forEach((design) => {
      const col = document.createElement("div");
      col.classList.add("col-sm-12", "col-md-6", "col-lg-4", "mt-2");

      const card = document.createElement("div");
      card.classList.add("card");

      const cardImage = document.createElement("img");
      cardImage.classList.add("card-image");
      cardImage.height = 200;
      cardImage.src = design.fields.image;

      card.appendChild(cardImage);

      const header = document.createElement("div");
      header.classList.add("card-header");

      const sellerImageContainer = document.createElement("span");

      const sellerImage = document.createElement("img");
      sellerImage.classList.add("rounded-circle");
      sellerImage.height = 50;
      sellerImage.width = 50;
      sellerImage.src =
        "https://i.pinimg.com/736x/8b/16/7a/8b167af653c2399dd93b952a48740620.jpg";

      sellerImageContainer.appendChild(sellerImage);
      header.appendChild(sellerImageContainer);

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

      header.appendChild(sellerInfo);
      card.appendChild(header);

      const cardBody = document.createElement("div");
      cardBody.classList.add("card-body", "text-dark");
      cardBody.id = "desc";

      const desc = document.createElement("p");
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
  }
}

getDesign();

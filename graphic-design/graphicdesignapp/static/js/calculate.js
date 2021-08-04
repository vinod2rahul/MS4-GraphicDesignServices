document.getElementById("calculate").addEventListener("click", async () => {
  const size = document.getElementById("size").value;
  const category = document.getElementById("cat").value;
  try {
    let data = new FormData();

    data.append("category", category);
    data.append("size", size);
    data.append("csrfmiddlewaretoken", "{{csrf_token}}");

    const res = await axios.post("/calculate-price/", data);
    const modalBody = document.getElementsByClassName("modal-body")[0];
    modalBody.innerHTML = `
      <div class="d-flex justify_content-between">Selected Category Price: ${res.data.category_price}</div>
      <div class="d-flex justify_content-between">Selected Size: ${res.data.desired_size}</div>
      <div class="d-flex justify_content-between">Price For Each px: ${res.data.price_per_each_px}</div>
      <div class="d-flex justify_content-between">Total Price: ${res.data.totalPrice}</div>
    `;
    document.getElementById("design-price").value = res.data.totalPrice;
  } catch (err) {
    alert(err.message);
  }
});

document.addEventListener("DOMContentLoaded", async () => {
  const size = document.getElementById("size").value;
  const category = document.getElementById("cat").value;
  try {
    let data = new FormData();

    data.append("category", category);
    data.append("size", size);
    data.append("csrfmiddlewaretoken", "{{csrf_token}}");

    const res = await axios.post("/calculate-price/", data);
    const modalBody = document.getElementsByClassName("modal-body")[0];
    modalBody.innerHTML = `
      <div class="d-flex justify_content-between">Selected Category Price: ${res.data.category_price}</div>
      <div class="d-flex justify_content-between">Selected Size: ${res.data.desired_size}</div>
      <div class="d-flex justify_content-between">Price For Each px: ${res.data.price_per_each_px}</div>
      <div class="d-flex justify_content-between">Total Price: ${res.data.totalPrice}</div>
    `;
    document.getElementById("design-price").value = res.data.totalPrice;
  } catch (err) {
    alert(err.message);
  }
});

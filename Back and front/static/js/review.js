document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("reviewForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      plant_id: plantId,
      author: document.getElementById("author").value,
      content: document.getElementById("content").value,
      rating: parseInt(document.getElementById("rating").value)
    };

    const res = await fetch("http://127.0.0.1:5000/reviews/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const result = await res.json();
    if (res.ok) {
      alert("¡Reseña enviada!");
      document.getElementById("reviewForm").reset();
    } else {
      alert("Error: " + result.error);
    }
  });
});

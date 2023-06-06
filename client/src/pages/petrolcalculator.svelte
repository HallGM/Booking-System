<script>
  import PetrolForm from "../components/PetrolForm.svelte";
  let quote = "";
  function calculateQuote({
    distance,
    cars,
    travelTimeHours,
    travelTimeMinutes,
    people,
  }) {
    let travelTime =
      travelTimeHours * 2 + Math.floor((travelTimeMinutes * 2) / 60);
    // 30p/mile + £5/hour/person
    let number = 0.3 * distance * 2 * cars + 5 * people * travelTime;
    quote = Math.round(number / 10) * 10;
  }
</script>

<div class="container">
  <h1 class="title is-3">Petrol Cost Calculator</h1>
  <div class="block">
    <p>( 30p/mile + £5/hour/person )</p>
  </div>
  <PetrolForm on:submitData={(e) => calculateQuote(e.detail)} />
  <div class="box">
    <h2 class="title is-4">Quote: {quote ? "£" + quote : ""}</h2>
  </div>
</div>

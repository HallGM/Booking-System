<script>
  import { createEventDispatcher } from "svelte";
  let distance = 0;
  let cars = 3;
  let travelTimeHours = 0;
  let travelTimeMinutes = 0;
  let people = 5;

  const dispatch = createEventDispatcher();

  function handleSubmit(e) {
    dispatch("submitData", { distance, cars, travelTimeHours, travelTimeMinutes, people });
  }
</script>

<form on:submit|preventDefault={handleSubmit}>
  <div class="field">
    <label class="label" for="distance">Distance to venue (miles):</label>
    <input
      bind:value={distance}
      type="number"
      name="distance"
      id="name"
      required
    />
  </div>
  <div class="field">
    <label class="label" for="travel-time-hours">Travel time to venue (hours):</label>
    <input bind:value={travelTimeHours} type="number" class="travel-time" id="travel-time-hours" required />
    <span >Hours</span>
    <input bind:value={travelTimeMinutes} type="number" class="travel-time" id="travel-time-minutes" required />
    <span >Minutes</span>
  </div>
  <div class="field">
    <label class="label" for="cars">Number of cars:</label>
    <input bind:value={cars} type="number" id="email" required />
  </div>
  <div class="field">
    <label class="label" for="people">Number of people:</label>
    <input bind:value={people} type="number" id="people" required />
  </div>
  
  <div class="field is-grouped">
    <div class="control">
      <button type="submit" class="button is-link">Calculate</button>
    </div>
  </div>

</form>

<style>
  .travel-time {
    width: 70px;
  }
</style>
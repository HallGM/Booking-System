<!-- 
  Example Usage:
  <Select
    bind:value={booking.status}
    options={[
      { displayName: "Enquired", value: "enquired" },
      { displayName: "Confirmed", value: "confirmed" },
    ]}
    label="Status"
    id="status"
  /> 
-->

<script>
  export let value;

  // Structure: {displayName: "Enquired", value: "enquired"}
  export let options;

  export let id = "";
  export let label = ""
</script>

<div class="field">
  <label class="label" for={id}>{label}</label>
  <div class="control">
    <div class="select">
      <select bind:value {id}>
        {#each options as option}
          <option value={option.value}>{option.displayName}</option>
        {/each}
      </select>
    </div>
  </div>
</div>

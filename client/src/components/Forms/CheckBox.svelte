<!-- 
  Example Usage:
  <CheckBox bind:value={booking.paid_deposit} id="paid_deposit" label="Paid Deposit" />

-->

<script>
    export let value;
    export let id = "";
    export let label = ""
  </script>

<div class="field">
  <div class="control">
    <label class="checkbox">
        <input type="checkbox" bind:checked={value} {id}/>
        {label}
    </label>
  </div>
</div>

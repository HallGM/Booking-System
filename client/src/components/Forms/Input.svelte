<!-- 
  Example Usage:
  
  <Input
    bind:value={booking.contact_full_names}
    label="Contact Full Name"
    id="contact_full_name"
    type="text"
  />
 -->
<script>
  export let value;
  export let type = "text";
  export let id = "";
  export let label = "";

  function typeAction(node) {
    node.type = type;
  }
</script>

<div class="field">
  <label class="label" for={id}>{label}</label>
  <div class="control">
    <input use:typeAction class="input" bind:value {id} />
  </div>
</div>

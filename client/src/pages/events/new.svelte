<script>
  import NewEnquiryForm from "../../components/NewEnquiryForm.svelte";
  import services from "../../services/booking";
  import { goto } from "@roxi/routify";
  import FullForm from "../../components/FullForm.svelte";

  function handleSubmit(e) {
    services.add(e.detail).then((ok) => {
      if (ok === "ok") {
        $goto("/events");
      }
    });
  }
  let moreOptions = false;
</script>
<style>
  button {
    margin-top: 10px;
  }
</style>
{#if moreOptions}
  <FullForm on:submit={handleSubmit} />
{:else}
  <NewEnquiryForm on:submit={handleSubmit} />
{/if}
<div class="container">
  <button class="button" on:click={() => (moreOptions = !moreOptions)}
    >{moreOptions ? "Less" : "More"} Options...</button
  >
</div>

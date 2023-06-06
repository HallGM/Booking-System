<script>
  import services from "../../../services/booking";
  import { params, goto, url } from "@roxi/routify";
  import FullForm from "../../../components/FullForm.svelte";

  let id = $params.id;
  let booking = services.get(id).then((booking) => {
    booking.convertDatesToISO();
    return booking;
  });

  function handleSubmit(data) {
    services.edit(id, data).then((res) => {
      if (res === "ok") $goto($url("/events/:id", id));
    });
  }
</script>

{#await booking}
  loading...
{:then booking}
  <FullForm {booking} on:submit={(res) => handleSubmit(res.detail)} />
{/await}

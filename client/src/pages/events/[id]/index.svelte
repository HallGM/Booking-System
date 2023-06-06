<script>
  import { params, url } from "@roxi/routify";
  import Card from "../../../components/Card.svelte";
  import InfoTable from "../../../components/InfoTable.svelte";
  import services from "../../../services/booking";
  const id = $params.id;
  const promise = services.get(id);

  function makeRow(field, value) {
    return { field, value };
  }
  function basicInfo(booking) {
    return [
      makeRow("Status", booking.status),
      makeRow("Contact Full Names", booking.contact_full_names),
      makeRow("Event Type", booking.event_type),
      makeRow("Event Date", booking.event_date_string()),
      makeRow("Venue", booking.venue),
      makeRow("Travel Cost", booking.travel_cost),
      makeRow("Set Option", booking.set_option),
      makeRow("Deposit", `${!booking.paid_deposit ? "Not" : ""} paid`),
    ];
  }
  function moreInfo(booking) {
    return [
      makeRow("Full Amount", `${!booking.paid_in_full ? "Not" : ""} paid`),
      makeRow("Quote", booking.quote),
      makeRow("Song Request", booking.song_request),
      makeRow("Setup Info", booking.setup_info),
      makeRow("Setup Info", booking.setup_info),
      makeRow("Music Between Sets", booking.music_between_sets),
      makeRow("Timings", booking.timings),
      makeRow("Any Other Info", booking.any_other_info),
    ];
  }
  function contactInfo(booking) {
    return [
      makeRow("Contact Telephone", booking.contact_telephone),
      makeRow("Contact Address", booking.contact_address),
    ];
  }
  function weddingOptions(booking) {
    return [
      makeRow("Theme", booking.wedding_theme),
      makeRow("Couple Introduced as", booking.introduced_as),
    ];
  }
  function enquiryDetails(booking) {
    return [
      makeRow("Name on Enquiry", booking.enquiry_name),
      makeRow("Enquiry Date", booking.enquiry_date_string()),
      makeRow("Enquiry Method", booking.enquiry_method),
      makeRow("Email Address", booking.enquiry_email),
    ];
  }
</script>

<div class="container">
  {#await promise}
    loading...
  {:then booking}
    <Card title="Basic Info">
      <InfoTable rows={basicInfo(booking)} />
    </Card>

    <Card title="More Info">
      <InfoTable rows={moreInfo(booking)} />
    </Card>

    <Card title="Contact Info">
      <InfoTable rows={contactInfo(booking)} />
    </Card>
    <Card title="Wedding Options">
      <InfoTable rows={weddingOptions(booking)} />
    </Card>

    <Card title="Enquiry Details">
      <InfoTable rows={enquiryDetails(booking)} />
    </Card>

    <span class="icon-text">
      <a href={$url("./edit")} class="button is-info is-light center">
        <span class="icon">
          <i class="fa-solid fa-pencil"></i>
        </span>
        &nbsp; Edit
      </a>
    </span>
    
  {/await}
</div>

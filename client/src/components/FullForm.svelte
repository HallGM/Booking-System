<script>
  import { createEventDispatcher } from "svelte";
  import { newBlankBooking, defaultFixTheMusic } from "../helpers/Booking";
  import Select from "./Forms/Select.svelte";
  import Input from "./Forms/Input.svelte";
  import CheckBox from "./Forms/CheckBox.svelte";

  export let booking;

  if (!booking) {
    booking = newBlankBooking();
  }

  const dispatch = createEventDispatcher();

  const handleSubmit = () => {
    dispatch("submit", booking);
  };

  function handleFixTheMusic() {
    defaultFixTheMusic(booking);
    booking = booking;
  }
</script>

<style>
  h1, h2 {
    margin-top: 30px;
  }
</style>

<div class="container">
  <h1 class="title">Contact Form</h1>
  <h2 class="subtitle">Defaults:</h2>
  <button class="button is-info" on:click={handleFixTheMusic}>Fix The Music</button>
  <form on:submit|preventDefault={handleSubmit}>
    <h2 class="subtitle">Basic Info</h2>

    <Select
      bind:value={booking.status}
      options={[
        { displayName: "Enquired", value: "enquired" },
        { displayName: "Confirmed", value: "confirmed" },
      ]}
      label="Status"
      id="status"
    />

    <Input
      bind:value={booking.contact_full_names}
      label="Contact Full Name"
      id="contact_full_name"
      type="text"
    />

    <Select
      bind:value={booking.status}
      options={[
        { displayName: "Wedding", value: "wedding" },
        { displayName: "Birthday", value: "birthday" },
        { displayName: "Pub", value: "pub" },
        { displayName: "Other", value: "other" },
      ]}
      label="Event Type"
      id="event_type"
    />

    <Input
      bind:value={booking.event_date}
      label="Date of Event"
      id="event_date"
      type="date"
    />

    <Input bind:value={booking.venue} label="Venue" id="venue" />

    <Input bind:value={booking.quote} label="Quote Given" id="quote" />

    <Input
      bind:value={booking.travel_cost}
      label="Travel Cost Quoted"
      id="travel_cost"
    />

    <Select
      bind:value={booking.set_option}
      options={[
        { displayName: "Standard", value: "standard" },
        { displayName: "Extended", value: "extended" },
        { displayName: "Unknown", value: "unknown" },
        { displayName: "Other", value: "other" },
      ]}
      label="Set Option"
      id="set_option"
    />
    <CheckBox
      bind:value={booking.paid_deposit}
      id="paid_deposit"
      label="Paid Deposit"
    />

    <CheckBox
      bind:value={booking.paid_in_full}
      id="paid_in_full"
      label="Paid in Full"
    />

    <h2 class="subtitle">Other Info</h2>

    <Input
      bind:value={booking.song_request}
      label="Song Request"
      id="song_request"
    />

    <Input bind:value={booking.setup_info} label="Setup Info" id="setup_info" />
    <Input
      bind:value={booking.music_between_sets}
      label="Music between Sets"
      id="music_between_sets"
    />

    <Input bind:value={booking.timings} label="Timings" id="timings" />

    <Input
      bind:value={booking.any_other_info}
      label="Any Other Info"
      id="other"
    />

    <h2 class="subtitle">Contact Info</h2>
    <Input
      bind:value={booking.contact_telephone}
      label="Contact Telephone"
      id="contact_telephone"
    />

    <Input
      bind:value={booking.contact_address}
      label="Contact Address"
      id="contact_address"
    />
    <h2 class="subtitle">Weddings</h2>

    <Input
      bind:value={booking.wedding_theme}
      label="Wedding Theme"
      id="wedding_theme"
    />

    <Input
      bind:value={booking.introduced_as}
      label="Couple Introduced As..."
      id="introduced_as"
    />
    <h2 class="subtitle">Enquiry</h2>

    <Input
      bind:value={booking.enquiry_name}
      label="Name of Enquirer"
      id="enquiry_name"
    />

    <Input
      bind:value={booking.enquiry_date}
      label="Date of Enquiry"
      id="enquiry_date"
      type="date"
    />

    <Input
      bind:value={booking.enquiry_method}
      label="Enquiry Method"
      id="enquiry_method"
    />

    <Input
      bind:value={booking.enquiry_email}
      label="Enquiry Email Address"
      id="enquiry_email"
    />

    <div>
      <button class="button is-primary" type="submit">Save</button>
    </div>
  </form>
</div>

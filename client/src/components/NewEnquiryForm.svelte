<script>
  import { createEventDispatcher } from "svelte";
  import { newBlankBooking } from "../helpers/Booking";

  import Select from "./Forms/Select.svelte";
  import Input from "./Forms/Input.svelte";

  const dispatch = createEventDispatcher();

  let booking = newBlankBooking();

  // let enquiry_name;
  // let enquiry_date;
  // let event_date;
  // let enquiry_method;
  // let enquiry_email;
  // let event_type;
  // let venue;
  // let quote;
  // let travel_cost;
  // let any_other_info;
  // let set_option;

  const handleSubmit = () => {
    booking.status = "enquired";
    booking.paid_deposit = false;
    booking.paid_in_full = false;
    dispatch("submit", booking);
  };
</script>

<div class="container">
  <h1 class="title">New Enquiry</h1>

  <form on:submit|preventDefault={handleSubmit}>
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
    <Input bind:value={booking.quote} label="Quote Given" id="quote" />
    <Input
      bind:value={booking.travel_cost}
      label="Travel Cost Quoted"
      id="travel_cost"
    />
    <Input
      bind:value={booking.any_other_info}
      label="Any Other Info"
      id="other"
    />

    <div>
      <button class="button is-primary" type="submit">Save</button>
    </div>
  </form>
</div>

<script>
  import { url } from "@roxi/routify";
  import services from "../../services/booking";

  const oneMonthAgo = new Date();
  oneMonthAgo.setMonth(oneMonthAgo.getMonth() - 1);

  let allBookings = [];

  function happened(date) {
    const now = new Date();
    return date.getTime() < now.getTime();
  }

  $: confirmed_events = allBookings.filter((booking) => {
    const date = new Date(booking.event_date);
    return !happened(date) && booking.status == "confirmed";
  });
  $: completed_events = allBookings.filter((booking) => {
    const date = new Date(booking.event_date);
    return happened(date) && booking.status == "confirmed";
  });
  $: enquiries = allBookings.filter((booking) => booking.status === "enquired");
  services.getAll().then((bookings) => (allBookings = bookings));

</script>

<div class="container">
  <div class="level">
    <h2 class="title">Enquiries</h2>
    <a class="button is-success" href={$url("./new")}>New Enquiry</a>
  </div>
  <table class="table is-bordered">
    <tbody>
      <tr>
        <th>Name</th>
        <th>Enquired</th>
        <th>Email</th>
      </tr>
      {#each enquiries as booking}
        <tr>
          <td
            ><a href={$url("./:id", { id: booking.id })}
              >{booking.enquiry_name}</a
            ></td
          >
          <td>{booking.enquiry_date_string()}</td>
          <td>{booking.enquiry_email}</td>

          <!-- <td
            ><a
              href={$url("./:id/edit", { id: booking.id })}
              class="button is-info is-light">edit</a
            ></td
          > -->
          <!-- <td
            ><button
              on:click={() => handleDelete(booking.id)}
              class="button is-danger">delete</button
            ></td
          > -->
        </tr>
      {/each}
    </tbody>
  </table>

  <h2 class="title">Confirmed Events</h2>
  {#if !confirmed_events.length}
    none...
  {:else}
    <table class="table is-bordered is-hoverable">
      <tbody>
        <tr>
          <th>Name</th>
          <th>Event Type</th>
          <th>Date</th>
          <th>Paid in full?</th>
          <th />
        </tr>
        {#each confirmed_events as booking}
          <tr>
            <td
              ><a href={$url("./:id", { id: booking.id })}>
                {booking.enquiry_name}</a
              >
            </td>
            <td>{booking.event_type}</td>
            <td>{booking.event_date_string()}</td>
            <td
              ><input type="checkbox" bind:checked={booking.paid_in_full} /></td
            >
            <!-- <td
              ><a
                href={$url("./:id/edit", { id: booking.id })}
                class="button is-info is-light">edit</a
              ></td
            > -->
          </tr>
        {/each}
      </tbody>
    </table>
  {/if}

  <h2 class="title">Completed Events</h2>
  <table class="table is-bordered">
    <tbody>
      <tr>
        <th>Name</th>
        <th>Event Type</th>
        <th>Date</th>
        <th>Payment</th>
        <th>Travel cost</th>
        
      </tr>
      {#each completed_events as booking}
        <tr>
          <td
            ><a href={$url("./:id", { id: booking.id })}
              >{booking.enquiry_name}</a
            ></td
          >
          <td>{booking.event_type}</td>
          <td>{booking.event_date_string()}</td>
          <td>£{booking.quote}</td>
          <td>£{booking.travel_cost}</td>
          <!-- <td
            ><a
              href={$url("./:id/edit", { id: booking.id })}
              class="button is-info is-light">edit</a
            ></td
          > -->
        </tr>
      {/each}
    </tbody>
  </table>
</div>

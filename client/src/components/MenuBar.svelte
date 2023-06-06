<script>
  import { url } from "@roxi/routify";

  let open = false;

  function toggle() {
    open = !open
  }
  const logoAddress = "https://www.radiopachuco.co.uk/wp-content/uploads/2016/06/Logo2.png"
  const hamburgerButtonID = "hamburger-button";
  const mobileMenuButtonID = "mobile-menu";

  document.addEventListener("click", handleClick, true);

  function handleClick(e) {
    const ids = [hamburgerButtonID, mobileMenuButtonID];
    if (ids.includes(e.target.id)) {
      return;
    }
    open = false;
  }
</script>

<nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href={$url("/events")}>
      <img
        alt="logo"
        src={logoAddress}
      />
    </a>

    <button
      on:click={toggle}
      role="button"
      class="navbar-burger"
      aria-label="menu"
      aria-expanded="false"
      data-target="navbarBasicExample"
      id={hamburgerButtonID}
    >
      <span aria-hidden="true" />
      <span aria-hidden="true" />
      <span aria-hidden="true" />
    </button>
  </div>
  {#if open}
    <div id={mobileMenuButtonID}>
      <a class="navbar-item" href={$url("/events")}>Events</a>
      <a class="navbar-item" href={$url("/petrolcalculator")}
        >Petrol Cost Calculator</a
      >
    </div>
  {/if}
  <div class="navbar-menu">
    <div class="navbar-start">
      <a class="navbar-item" href={$url("/events")}>Events</a>
      <a class="navbar-item" href={$url("/petrolcalculator")}
        >Petrol Cost Calculator</a
      >
    </div>
  </div>
</nav>

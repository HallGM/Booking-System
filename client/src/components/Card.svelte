<script>
  export let title = null;
</script>

<div class="card">
  {#if title}
    <header class="card-header">
      <p class="card-header-title">
        {title}
      </p>
    </header>
  {/if}
  <div class="card-content">
    <div class="content">
      <slot />
    </div>
  </div>
</div>

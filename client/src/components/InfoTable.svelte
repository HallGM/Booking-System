<script>
  export let rows = [{ field: "", value: "" }];
  let midpoint = Math.floor(rows.length / 2);
  let rowrows = [rows.slice(0, midpoint), rows.slice(midpoint, rows.length)];
  $: console.log(rows);
  $: console.log(rowrows);
</script>

{#each rowrows as rows_}
<table class="table is-bordered" style="margin:0">
  <tbody style="display:flex; flex-wrap: wrap">
      <div style="flex-grow: 1; width: 300px; flex-shrink: 1">
        {#each rows_ as row}
          <tr style="display:flex">
            <td style="text-align:right; width:50%">
              <strong>{row.field}:</strong>
            </td>
            <td style="width:50%">{row.value}</td>
          </tr>
        {/each}
      </div>
    </tbody>
  </table>
  {/each}

<style>
  td {
  }
  td:empty {
    text-align: left;
  }
  td:empty:before {
    content: "-";
  }
</style>

<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import Quill from 'quill';
  import 'quill/dist/quill.snow.css';
  import MarkdownShortcuts from 'quill-markdown-shortcuts';

  Quill.register('modules/markdownShortcuts', MarkdownShortcuts);

  let editorElement: HTMLElement;
  let quill: any;

  onMount(() => {
    quill = new Quill(editorElement, {
      theme: 'snow',
      modules: {
        markdownShortcuts: {},
        toolbar: [
          ['bold', 'italic', 'underline', 'strike'],
          ['blockquote', 'code-block'],
          [{ 'header': 1 }, { 'header': 2 }],
          [{ 'list': 'ordered'}, { 'list': 'bullet' }],
          [{ 'script': 'sub'}, { 'script': 'super' }],
          [{ 'indent': '-1'}, { 'indent': '+1' }],
          [{ 'direction': 'rtl' }],
          [{ 'size': ['small', false, 'large', 'huge'] }],
          [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
          [{ 'color': [] }, { 'background': [] }],
          [{ 'font': [] }],
          [{ 'align': [] }],
          ['clean']
        ]
      }
    });
  });

  onDestroy(() => {
    if (quill) {
      // Clean up if necessary
    }
  });
</script>

<div class="h-full flex flex-col bg-white dark:bg-gray-850">
  <div bind:this={editorElement} class="flex-1 overflow-y-auto" />
</div>

<style>
  :global(.ql-toolbar) {
    border-top: none !important;
    border-left: none !important;
    border-right: none !important;
    border-bottom: 1px solid #e5e7eb !important;
  }

  :global(.ql-container) {
    border: none !important;
  }

  :global(.dark .ql-toolbar) {
    border-color: #1f2937 !important;
  }

  :global(.dark .ql-toolbar button) {
    color: #e5e7eb;
  }

  :global(.dark .ql-toolbar button:hover) {
    color: #ffffff;
  }

  :global(.dark .ql-toolbar .ql-stroke) {
    stroke: #e5e7eb;
  }

  :global(.dark .ql-toolbar .ql-fill) {
    fill: #e5e7eb;
  }

  :global(.dark .ql-toolbar .ql-picker) {
    color: #e5e7eb;
  }

  :global(.dark .ql-editor) {
    color: #e5e7eb;
  }

  :global(.dark .ql-editor.ql-blank::before) {
    color: #6b7280;
  }
</style> 
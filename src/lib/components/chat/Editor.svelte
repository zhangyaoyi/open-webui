<script lang="ts">
	import { onMount, onDestroy, createEventDispatcher } from 'svelte';
	import Quill from 'quill';
	import 'quill/dist/quill.snow.css';
	import MarkdownShortcuts from 'quill-markdown-shortcuts';
	import { getEditorContent, saveEditorContent } from '$lib/apis/editor';

	Quill.register('modules/better-table', QuillBetterTable);
	Quill.register('modules/markdownShortcuts', MarkdownShortcuts);

	let editorElement: HTMLElement;
	let quill: any;
	const dispatch = createEventDispatcher();

	export let content = '';
	export let chatId: string | undefined = undefined;
	let saving = false;
	let error = '';

	onMount(async () => {
		quill = new Quill(editorElement, {
			theme: 'snow',
			modules: {
				markdownShortcuts: {},
				'better-table': true,
				toolbar: [
					['bold', 'italic', 'underline', 'strike'],
					['blockquote', 'code-block'],
					[{ header: 1 }, { header: 2 }],
					[{ list: 'ordered' }, { list: 'bullet' }],
					[{ script: 'sub' }, { script: 'super' }],
					[{ indent: '-1' }, { indent: '+1' }],
					[{ direction: 'rtl' }],
					[{ size: ['small', false, 'large', 'huge'] }],
					[{ header: [1, 2, 3, 4, 5, 6, false] }],
					[{ color: [] }, { background: [] }],
					[{ font: [] }],
					[{ align: [] }],
					['clean']
				]
			}
		});

		// Initialize content
		try {
			// If we have prop content, use it
			if (content) {
				quill.root.innerHTML = content;
			} else if (chatId) { // Only try to load from server if we have a chatId
				// Otherwise load from server
				const res = await getEditorContent(localStorage.token, chatId);
				if (res?.content) {
					quill.root.innerHTML = res.content;
					content = res.content; // Update the prop
				}
			}
		} catch (e) {
			error = e instanceof Error ? e.message : 'Failed to load content';
			console.error('Failed to load editor content:', e);
		}

		// Listen for content changes
		quill.on('text-change', async () => {
			const newContent = quill.root.innerHTML;
			content = newContent;
			
			if (saving || !chatId) return; // Don't save if we don't have a chatId
			
			try {
				saving = true;
				await saveEditorContent(localStorage.token, chatId, newContent);
				error = '';
			} catch (e) {
				error = e instanceof Error ? e.message : 'Failed to save content';
				console.error('Failed to save editor content:', e);
			} finally {
				saving = false;
			}
		});
	});

	onDestroy(() => {
		if (quill) {
			quill.off('text-change');
		}
	});
</script>

<div class="h-full flex flex-col bg-white dark:bg-gray-850">
	<div bind:this={editorElement} class="flex-1 overflow-y-auto" />
	{#if error}
		<div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4" role="alert">
			{error}
		</div>
	{/if}
	{#if saving}
		<div class="mt-2 text-sm text-gray-500">Saving...</div>
	{/if}
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

	:global(.ql-snow .ql-editor) {
		font-size: medium !important;
	}
</style>

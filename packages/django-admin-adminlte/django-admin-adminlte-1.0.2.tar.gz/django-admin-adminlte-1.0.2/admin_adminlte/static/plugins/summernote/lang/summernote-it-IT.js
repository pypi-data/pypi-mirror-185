/*!
 * 
 * Super simple WYSIWYG editor v0.8.20
 * https://summernote.org
 *
 *
 * Copyright 2013- Alan Hong and contributors
 * Summernote may be freely distributed under the MIT license.
 *
 * Date: 2021-10-14T21:15Z
 *
 */
(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory();
	else if(typeof define === 'function' && define.amd)
		define([], factory);
	else {
		var a = factory();
		for(var i in a) (typeof exports === 'object' ? exports : root)[i] = a[i];
	}
})(self, function() {
return /******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
(function ($) {
  $.extend($.summernote.lang, {
    'it-IT': {
      font: {
        bold: 'Testo in grassetto',
        italic: 'Testo in corsivo',
        underline: 'Testo sottolineato',
        clear: 'Elimina la formattazione del testo',
        height: 'Altezza della linea di testo',
        name: 'Famiglia Font',
        strikethrough: 'Testo barrato',
        subscript: 'Subscript',
        superscript: 'Superscript',
        size: 'Dimensione del carattere'
      },
      image: {
        image: 'Immagine',
        insert: 'Inserisci Immagine',
        resizeFull: 'Dimensioni originali',
        resizeHalf: 'Ridimensiona al 50%',
        resizeQuarter: 'Ridimensiona al 25%',
        floatLeft: 'Posiziona a sinistra',
        floatRight: 'Posiziona a destra',
        floatNone: 'Nessun posizionamento',
        shapeRounded: 'Shape: Rounded',
        shapeCircle: 'Shape: Circle',
        shapeThumbnail: 'Shape: Thumbnail',
        shapeNone: 'Shape: None',
        dragImageHere: 'Trascina qui un\'immagine',
        dropImage: 'Drop image or Text',
        selectFromFiles: 'Scegli dai Documenti',
        maximumFileSize: 'Maximum file size',
        maximumFileSizeError: 'Maximum file size exceeded.',
        url: 'URL dell\'immagine',
        remove: 'Rimuovi immagine',
        original: 'Original'
      },
      video: {
        video: 'Video',
        videoLink: 'Collegamento ad un Video',
        insert: 'Inserisci Video',
        url: 'URL del Video',
        providers: '(YouTube, Vimeo, Vine, Instagram, DailyMotion o Youku)'
      },
      link: {
        link: 'Collegamento',
        insert: 'Inserisci Collegamento',
        unlink: 'Elimina collegamento',
        edit: 'Modifica collegamento',
        textToDisplay: 'Testo del collegamento',
        url: 'URL del collegamento',
        openInNewWindow: 'Apri in una nuova finestra'
      },
      table: {
        table: 'Tabella',
        addRowAbove: 'Add row above',
        addRowBelow: 'Add row below',
        addColLeft: 'Add column left',
        addColRight: 'Add column right',
        delRow: 'Delete row',
        delCol: 'Delete column',
        delTable: 'Delete table'
      },
      hr: {
        insert: 'Inserisce una linea di separazione'
      },
      style: {
        style: 'Stili',
        p: 'pe',
        blockquote: 'Citazione',
        pre: 'Codice',
        h1: 'Titolo 1',
        h2: 'Titolo 2',
        h3: 'Titolo 3',
        h4: 'Titolo 4',
        h5: 'Titolo 5',
        h6: 'Titolo 6'
      },
      lists: {
        unordered: 'Elenco non ordinato',
        ordered: 'Elenco ordinato'
      },
      options: {
        help: 'Aiuto',
        fullscreen: 'Modalità a tutto schermo',
        codeview: 'Visualizza codice'
      },
      paragraph: {
        paragraph: 'Paragrafo',
        outdent: 'Diminuisce il livello di rientro',
        indent: 'Aumenta il livello di rientro',
        left: 'Allinea a sinistra',
        center: 'Centra',
        right: 'Allinea a destra',
        justify: 'Giustifica (allinea a destra e sinistra)'
      },
      color: {
        recent: 'Ultimo colore utilizzato',
        more: 'Altri colori',
        background: 'Colore di sfondo',
        foreground: 'Colore',
        transparent: 'Trasparente',
        setTransparent: 'Trasparente',
        reset: 'Reimposta',
        resetToDefault: 'Reimposta i colori'
      },
      shortcut: {
        shortcuts: 'Scorciatoie da tastiera',
        close: 'Chiudi',
        textFormatting: 'Formattazione testo',
        action: 'Azioni',
        paragraphFormatting: 'Formattazione paragrafo',
        documentStyle: 'Stili',
        extraKeys: 'Extra keys'
      },
      help: {
        'insertParagraph': 'Insert Paragraph',
        'undo': 'Undoes the last command',
        'redo': 'Redoes the last command',
        'tab': 'Tab',
        'untab': 'Untab',
        'bold': 'Set a bold style',
        'italic': 'Set a italic style',
        'underline': 'Set a underline style',
        'strikethrough': 'Set a strikethrough style',
        'removeFormat': 'Clean a style',
        'justifyLeft': 'Set left align',
        'justifyCenter': 'Set center align',
        'justifyRight': 'Set right align',
        'justifyFull': 'Set full align',
        'insertUnorderedList': 'Toggle unordered list',
        'insertOrderedList': 'Toggle ordered list',
        'outdent': 'Outdent on current paragraph',
        'indent': 'Indent on current paragraph',
        'formatPara': 'Change current block\'s format as a paragraph(P tag)',
        'formatH1': 'Change current block\'s format as H1',
        'formatH2': 'Change current block\'s format as H2',
        'formatH3': 'Change current block\'s format as H3',
        'formatH4': 'Change current block\'s format as H4',
        'formatH5': 'Change current block\'s format as H5',
        'formatH6': 'Change current block\'s format as H6',
        'insertHorizontalRule': 'Insert horizontal rule',
        'linkDialog.show': 'Show Link Dialog'
      },
      history: {
        undo: 'Annulla',
        redo: 'Ripristina'
      },
      specialChar: {
        specialChar: 'SPECIAL CHARACTERS',
        select: 'Select Special characters'
      }
    }
  });
})(jQuery);
/******/ 	return __webpack_exports__;
/******/ })()
;
});
//# sourceMappingURL=summernote-it-IT.js.map
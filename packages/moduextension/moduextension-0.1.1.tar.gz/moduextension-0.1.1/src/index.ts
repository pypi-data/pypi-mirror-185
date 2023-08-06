import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin,
} from "@jupyterlab/application";

import { MainAreaWidget } from "@jupyterlab/apputils";

import { ILauncher } from "@jupyterlab/launcher";

import { LabIcon, reactIcon } from "@jupyterlab/ui-components";

import { ModuCodingWidget } from "./widget";

/**
 * The command IDs used by the react-widget plugin.
 */
namespace CommandIDs {
  export const create = "create-react-widget";
}

/**
 * Initialization data for the react-widget extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: "modu-jupyter-extension",
  autoStart: true,
  optional: [ILauncher],
  activate: (app: JupyterFrontEnd, launcher: ILauncher) => {
    const { commands } = app;

    // 커스텀 아이콘은 svg에서 생성가능.
    const moduIcon = new LabIcon({
      name: "moduIcon",
      svgstr: `<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 23.98"><defs><style>.cls-1{fill:none;}.cls-2{fill:#212435;}.cls-3{fill:#495ef1;}.cls-4{fill:#d64c32;}</style></defs><rect class="cls-1" width="52" height="23.98"/><path class="cls-2" d="M463,141.7V140h1.17v1.74h3.2v1h-6.79v-1Zm1.94-.78a1.94,1.94,0,0,0,.34-.84,7.58,7.58,0,0,0,.06-.76h-4.13v-1h4.14v-1h-4.18v-1h5.32v3.09a4.93,4.93,0,0,1,0,.55,3.81,3.81,0,0,1-.12.51,1.08,1.08,0,0,1-.24.39Z" transform="translate(-422.13 -130.96)"/><path class="cls-2" d="M446.58,140.1a2.11,2.11,0,0,0,.71.43,3,3,0,0,0,.85.22,4.14,4.14,0,0,0,.94.05,5.74,5.74,0,0,0,.93-.08,5,5,0,0,0,.87-.22,3.63,3.63,0,0,0,.72-.31v-1a4.87,4.87,0,0,1-1.48.49,5,5,0,0,1-1.47.07,2.6,2.6,0,0,1-1.13-.33.77.77,0,0,1-.46-.72v-1.37h4.41v-1h-5.53v2.18a2,2,0,0,0,.18.89A1.83,1.83,0,0,0,446.58,140.1Z" transform="translate(-422.13 -130.96)"/><polygon class="cls-2" points="23.4 11.58 26.23 11.58 26.23 13.6 27.39 13.6 27.39 11.58 30.19 11.58 30.19 10.62 23.4 10.62 23.4 11.58"/><polygon class="cls-2" points="36.27 5.2 36.27 11.68 37.38 11.69 37.38 5.2 36.27 5.2"/><rect class="cls-2" x="30.8" y="10.62" width="5" height="0.93"/><path class="cls-2" d="M455.28,136.08a2.35,2.35,0,1,0,2.34,2.35A2.35,2.35,0,0,0,455.28,136.08Zm0,3.59a1.25,1.25,0,1,1,1.24-1.24A1.25,1.25,0,0,1,455.28,139.67Z" transform="translate(-422.13 -130.96)"/><path class="cls-2" d="M470.84,140.79a2.7,2.7,0,0,0,.68-.22,2.33,2.33,0,0,0,.57-.34v-1a3.39,3.39,0,0,1-1.22.51,2.33,2.33,0,0,1-1.05,0,1.17,1.17,0,0,1-.74-.42,1.11,1.11,0,0,1-.28-.79v-1.22h2.76v-1h-3.89v2.07a2.52,2.52,0,0,0,.14.91,1.74,1.74,0,0,0,.37.67,1.76,1.76,0,0,0,.55.46,1.92,1.92,0,0,0,.66.27,3.55,3.55,0,0,0,1.45,0Z" transform="translate(-422.13 -130.96)"/><path class="cls-2" d="M474.12,143h0v-6.81H473v5a2.16,2.16,0,1,0,1.12,1.9ZM472,144.06a1,1,0,1,1,1.05-1A1,1,0,0,1,472,144.06Z" transform="translate(-422.13 -130.96)"/><path class="cls-1" d="M443.09,138.93v-1.58H440v1.59a1,1,0,0,0,.33.83,1.34,1.34,0,0,0,.88.27h.63a1.55,1.55,0,0,0,.91-.27A1,1,0,0,0,443.09,138.93Z" transform="translate(-422.13 -130.96)"/><path class="cls-2" d="M442.17,141.62V141a2.38,2.38,0,0,0,1.38-.49,1.79,1.79,0,0,0,.66-1.49v-2.61h-5.35v2.51a1.89,1.89,0,0,0,.63,1.56A2.34,2.34,0,0,0,441,141v.64h-2.82v.95H445v-.95Zm-1-1.58a1.34,1.34,0,0,1-.88-.27,1,1,0,0,1-.33-.83v-1.59h3.12v1.58a1,1,0,0,1-.37.84,1.55,1.55,0,0,1-.91.27Z" transform="translate(-422.13 -130.96)"/><path class="cls-3" d="M435,137.19v1.29c0,.61.34.84.91,1a.86.86,0,0,1,0,1.65c-.61.13-.91.36-.91,1v1.25c0,1.09-.65,2.07-2.35,2.14-.41,0-.55-.23-.55-.59a.54.54,0,0,1,.53-.62,1,1,0,0,0,1-1v-1.37a1.35,1.35,0,0,1,1.21-1.56v-.05c-1.08-.2-1.21-.87-1.21-1.64v-1.36a1,1,0,0,0-1-1c-.4,0-.54-.31-.54-.66s.14-.56.47-.56C434.34,135,435,136.09,435,137.19Z" transform="translate(-422.13 -130.96)"/><path class="cls-3" d="M423.67,143.31V142c0-.62-.35-.85-.92-1a.74.74,0,0,1-.62-.82.72.72,0,0,1,.62-.83c.62-.13.92-.37.92-1v-1.25c0-1.09.65-2.07,2.35-2.13.41,0,.55.22.55.58a.55.55,0,0,1-.53.63,1,1,0,0,0-1,1v1.37a1.35,1.35,0,0,1-1.21,1.56v.06c1.08.19,1.21.86,1.21,1.64v1.35a1,1,0,0,0,1,1c.4,0,.54.3.54.65s-.14.57-.47.57C424.32,145.47,423.67,144.41,423.67,143.31Z" transform="translate(-422.13 -130.96)"/><circle class="cls-3" cx="5.41" cy="8.09" r="0.81"/><circle class="cls-3" cx="8.99" cy="8.02" r="0.81"/><path class="cls-3" d="M430.89,141.28a2,2,0,0,1-3.13,0c-.43-.48-1.13.23-.7.71a3,3,0,0,0,4.54,0c.43-.48-.28-1.19-.71-.71Z" transform="translate(-422.13 -130.96)"/><path class="cls-4" d="M50.22,17.18h0a.35.35,0,0,1,.35.35v.76a.35.35,0,0,1-.35.35H50a.15.15,0,0,1-.15-.15v-1A.35.35,0,0,1,50.22,17.18Z"/><path class="cls-4" d="M473.78,153.34h-.67a.42.42,0,0,1-.42-.42v-2.06h1.09a.35.35,0,0,0,0-.7h-1.62a.16.16,0,0,0-.16.16v2.58a1.36,1.36,0,0,0,0,.16,1.1,1.1,0,0,0,1.1,1h.67a.35.35,0,1,0,0-.69Z" transform="translate(-422.13 -130.96)"/><path class="cls-4" d="M471.07,150.47a1.46,1.46,0,0,0-1.19-.5,1.43,1.43,0,0,0-1.14.49,1.87,1.87,0,0,0-.43,1.32v.46a1.85,1.85,0,0,0,.44,1.32,1.5,1.5,0,0,0,1.2.47,2.29,2.29,0,0,0,.83-.14l.42-.2.07-.06,0,0a.31.31,0,0,0,.07-.21.32.32,0,0,0-.33-.32.31.31,0,0,0-.13,0h0a2.23,2.23,0,0,1-.31.15,1.57,1.57,0,0,1-.6.1.82.82,0,0,1-.68-.28,1.17,1.17,0,0,1-.26-.79h2a.44.44,0,0,0,.44-.48v0A2,2,0,0,0,471.07,150.47Zm-1.82.44a.74.74,0,0,1,.63-.28.82.82,0,0,1,.66.27,1.14,1.14,0,0,1,.26.76H469A1.24,1.24,0,0,1,469.25,150.91Z" transform="translate(-422.13 -130.96)"/><path class="cls-4" d="M458.24,150a1.73,1.73,0,0,0-1,.32v-1.8a.35.35,0,0,0-.35-.35h0a.35.35,0,0,0-.35.35v5.19a.35.35,0,0,0,.35.35h0a.35.35,0,0,0,.35-.35v-2h0a1,1,0,0,1,2,0v2a.35.35,0,0,0,.35.35h0a.35.35,0,0,0,.35-.35v-2A1.7,1.7,0,0,0,458.24,150Z" transform="translate(-422.13 -130.96)"/><path class="cls-4" d="M464.74,154a.35.35,0,0,0,.35-.35v-2h0a1,1,0,1,1,2,0v2a.36.36,0,0,0,.36.35h0a.35.35,0,0,0,.35-.35v-2a1.71,1.71,0,1,0-3.41,0h0v2a.36.36,0,0,0,.36.35Z" transform="translate(-422.13 -130.96)"/><path class="cls-4" d="M463.51,150.16a.35.35,0,0,0-.35.35v2h0a1,1,0,0,1-2,0v-2a.35.35,0,0,0-.35-.35h0a.35.35,0,0,0-.35.35v2a1.7,1.7,0,1,0,3.4,0h0v-2a.35.35,0,0,0-.35-.35Z" transform="translate(-422.13 -130.96)"/></svg>`,
    });

    app.shell.title.icon = moduIcon;
    //app.shell.title.label = "KT Aivle School";
    app.shell.title.label = "모두의 코딩"

    const command = CommandIDs.create;
    commands.addCommand(command, {
      // caption: "KT Aivle School",
      caption: "모두의 코딩",
      //label: (args) => (args["isPalette"] ? null : "KT Aivle School"),
      label: (args) => (args["isPalette"] ? null : "모두의 코딩"),
      icon: (args) => (args["isPalette"] ? null : moduIcon),
      execute: () => {
        const content = new ModuCodingWidget();
        const widget = new MainAreaWidget<ModuCodingWidget>({ content });
        //widget.title.label = "KT Aivle School";
        widget.title.label = "모두의 코딩";
        widget.title.icon = moduIcon;
        app.shell.add(widget, "main");
      },
    });

    if (launcher) {
      launcher.add({
        command,
      });
    }
  },
};

export default extension;

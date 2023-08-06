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
      svgstr: `<svg width="24" height="18" viewBox="0 0 24 18" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M14.5622 2.30139C14.7245 2.05809 14.8111 1.77206 14.8111 1.47945C14.8111 1.08708 14.6555 0.710771 14.3784 0.433321C14.1014 0.15587 13.7257 0 13.3339 0C13.0417 0 12.7561 0.0867679 12.5132 0.249332C12.2703 0.411896 12.0809 0.642955 11.9691 0.913289C11.8573 1.18362 11.828 1.48109 11.885 1.76808C11.942 2.05506 12.0827 2.31868 12.2893 2.52558C12.4959 2.73249 12.7591 2.87339 13.0457 2.93047C13.3322 2.98756 13.6293 2.95826 13.8992 2.84629C14.1691 2.73431 14.3998 2.54468 14.5622 2.30139ZM16.8982 5.01556L23.4786 16.2235L23.4898 16.2179C23.5969 16.3969 23.6547 16.6011 23.657 16.8098C23.6594 17.0184 23.6063 17.224 23.5033 17.4053C23.4002 17.5866 23.2509 17.7373 23.0705 17.8418C22.8902 17.9463 22.6853 18.0009 22.477 18H8.75667C8.44354 18 8.14324 17.8754 7.92182 17.6537C7.70041 17.4319 7.57602 17.1311 7.57602 16.8175C7.57602 16.5039 7.70041 16.2032 7.92182 15.9814C8.14324 15.7597 8.44354 15.6351 8.75667 15.6351H12.9869L8.04044 7.84558L2.18749 17.434C2.08138 17.6058 1.9331 17.7475 1.75678 17.8456C1.58046 17.9437 1.38199 17.9949 1.18029 17.9944C0.962945 17.9952 0.749722 17.935 0.564772 17.8207C0.297704 17.6571 0.106416 17.3941 0.032965 17.0893C-0.0404857 16.7845 0.00991549 16.4631 0.173085 16.1955L7.01086 4.98755C7.11636 4.81772 7.26296 4.67732 7.43707 4.57936C7.61118 4.48139 7.80717 4.42904 8.00687 4.42715C8.20667 4.42852 8.40287 4.48065 8.57707 4.57866C8.75127 4.67668 8.89777 4.81736 9.00288 4.98755L15.5329 15.254C15.6073 15.3728 15.6603 15.5036 15.6896 15.6407H20.4066L14.8614 6.21482C14.7026 5.94432 14.6576 5.62172 14.7364 5.318C14.8151 5.01427 15.011 4.7543 15.2811 4.59527C15.5512 4.43624 15.8733 4.39117 16.1766 4.47C16.4798 4.54882 16.7394 4.74506 16.8982 5.01556Z" fill="#19BEC9"/>
</svg>`,
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

import {Inject, Injectable} from '@angular/core';
import {DOCUMENT} from "@angular/common";

@Injectable({
  providedIn: 'root'
})
export class ThemeService {

  constructor(@Inject(DOCUMENT) private document: Document) {
  }

  switchTheme(theme: string) {
    let themeLink = this.document.getElementById('app-theme') as HTMLLinkElement;

    if (themeLink) {
      themeLink.href = theme + '.css';
    }
  }

  getAvailableThemes(): Theme[] {
    return [
      {
        name: "Lara blue",
        bundle: "lara-light-blue",
        icon: "pi pi-sun",
      },
      {
        name: "Lara blue",
        bundle: "lara-dark-blue",
        icon: "pi pi-moon",
      },
      {
        name: "Bootstrap purple",
        bundle: "bootstrap-light-purple",
        icon: "pi pi-sun",
      },
      {
        name: "Bootstrap purple",
        bundle: "bootstrap-dark-purple",
        icon: "pi pi-moon",
      },
      {
        name: "Indigo",
        bundle: "md-light-indigo",
        icon: "pi pi-sun",
      },
      {
        name: "Indigo",
        bundle: "md-dark-indigo",
        icon: "pi pi-moon",
      },
      {
        name: "Soho",
        bundle: "soho-light",
        icon: "pi pi-sun",
      },
      {
        name: "Soho",
        bundle: "soho-dark",
        icon: "pi pi-moon",
      },
      {
        name: "Viva",
        bundle: "viva-light",
        icon: "pi pi-sun",
      },
      {
        name: "Viva",
        bundle: "viva-dark",
        icon: "pi pi-moon",
      },
      {
        name: "Fluent",
        bundle: "fluent-light",
        icon: "pi pi-sun",
      },
      {
        name: "Mira",
        bundle: "mira",
        icon: "pi pi-sun",
      },
      {
        name: "Nano",
        bundle: "nano",
        icon: "pi pi-sun",
      },
      {
        name: "Saga green",
        bundle: "saga-green",
        icon: "pi pi-sun",
      },
      {
        name: "Luna Pink",
        bundle: "luna-pink",
        icon: "pi pi-moon",
      },
      {
        name: "Rhea",
        bundle: "rhea",
        icon: "pi pi-sun",
      },
      {
        name: "Nova",
        bundle: "nova",
        icon: "pi pi-sun",
      },
      {
        name: "Vela Orange",
        bundle: "vela-orange",
        icon: "pi pi-moon",
      },
      {
        name: "Arya Purple",
        bundle: "arya-purple",
        icon: "pi pi-moon",
      },
    ];
  }
}

export interface Theme {
  name: string,
  bundle: string,
  icon: 'pi pi-sun' | 'pi pi-moon'
}

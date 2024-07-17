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
        name: "Lara light blue",
        bundle: "lara-light-blue"
      },
      {
        name: "Lara dark blue",
        bundle: "lara-dark-blue"
      },
      {
        name: "Bootstrap light purple",
        bundle: "bootstrap-light-purple"
      },
      {
        name: "Bootstrap dark purple",
        bundle: "bootstrap-dark-purple"
      },
    ];
  }
}

export interface Theme {
  name: string,
  bundle: string,
}

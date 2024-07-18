import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, NavigationEnd, Router, RouterLink} from "@angular/router";
import {CommonModule} from "@angular/common";
import {BreadcrumbModule} from "primeng/breadcrumb";
import {MenuItem} from "primeng/api";
import {filter} from "rxjs/operators";

@Component({
  selector: 'app-breadcrumb',
  templateUrl: './breadcrumb.component.html',
  styleUrls: ['./breadcrumb.component.css'],
  imports: [
    RouterLink,
    CommonModule,
    BreadcrumbModule
  ],
  standalone: true
})
export class BreadcrumbComponent implements OnInit {
  home: MenuItem = {icon: 'pi pi-home', routerLink: '/'};
  breadcrumbs: MenuItem[] = [];

  constructor(private router: Router, private activatedRoute: ActivatedRoute) {
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd)
    ).subscribe(() => {
      this.breadcrumbs = this.createBreadcrumbs(this.activatedRoute.root);
      if (this.breadcrumbs && this.breadcrumbs.length > 1) {
        this.breadcrumbs.at(-1)!.url = undefined;
      }
    });
  }

  private createBreadcrumbs(route: ActivatedRoute, url: string = '', breadcrumbs: MenuItem[] = []): MenuItem[] {
    const children: ActivatedRoute[] = route.children;

    if (children.length === 0) {
      return breadcrumbs;
    }

    for (const child of children) {
      const routeURL: string = child.snapshot.url.map(segment => segment.path).join('/');
      if (routeURL !== '') {
        url += `/${routeURL}`;
      }

      let breadcrumb: MenuItem = {routerLink: url};
      let label = child.snapshot.data['breadcrumb'];
      let icon = child.snapshot.data['icon'];
      if (label) {
        breadcrumb.label = label;
        breadcrumbs.push(breadcrumb);
      } else if (icon) {
        breadcrumb.icon = icon;
        breadcrumbs.push(breadcrumb);
      }

      return this.createBreadcrumbs(child, url, breadcrumbs);
    }

    return breadcrumbs;
  }

  ngOnInit(): void {
  }
}

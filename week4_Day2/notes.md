- in a css style if there are two declaration which are the same the lower one overrides the above (-Cascading)
- class selectors are of a higher priority then element selectors
- ```css
      #cool{
          color: plum
      }
  <p id = 'cool'>This is super cool</p>
  ```

- !important(UN) > inline(president) > id (mom) > class(father) > p (element): Pe
- you should only use id once in an HTML file, you can't use it multiple times
- the **important** keyword.

```css
p {
  color: crimson !important;
}
```

<!-- 1. Create one more class
    2. Overridethe the class -->

### pseudo Class

Fake class that CSS assigns when user interacts

- fake - class
- Targets Mouse hover
- :hover

- Targets Click
- : actice

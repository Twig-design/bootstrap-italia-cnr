/**
 * --------------------------------------------------------------------------
 * Bootstrap Italia (https://italia.github.io/bootstrap-italia/)
 * Authors: https://github.com/italia/bootstrap-italia/blob/main/AUTHORS
 * Licensed under BSD-3-Clause license (https://github.com/italia/bootstrap-italia/blob/main/LICENSE)
 * --------------------------------------------------------------------------
 */

import Dropdown from './dropdown'

const SELECTOR_AUDIENCE_TOGGLE = '.it-header-audience-pills [data-bs-toggle="dropdown"], .it-header-audience-extra [data-bs-toggle="dropdown"]'
const SELECTOR_AUDIENCE_CONTENT = '.it-header-audience-content'

/**
 * Align the audience-bar dropdown menu to the full width and bottom of the
 * `.it-header-audience-content` container. The small notch (:before) is kept
 * horizontally centred on the clicked toggle.
 */
const initHeaderAudienceDropdowns = () => {
  if (typeof document === 'undefined') {
    return
  }

  const toggles = document.querySelectorAll(SELECTOR_AUDIENCE_TOGGLE)

  toggles.forEach((toggle) => {
    const content = toggle.closest(SELECTOR_AUDIENCE_CONTENT)

    if (!content) {
      return
    }

    // Use the whole content block as Popper reference so the menu opens
    // aligned to its left edge and bottom. Bootstrap's data-api reuses this
    // instance when the user clicks the toggle.
    new Dropdown(toggle, {
      reference: content,
      offset: () => {
        const menu = toggle.parentElement.querySelector('.dropdown-menu')

        if (!menu) {
          return [0, 0]
        }

        const contentRect = content.getBoundingClientRect()
        const toggleRect = toggle.getBoundingClientRect()
        const notchSize = parseFloat(getComputedStyle(menu).getPropertyValue('--bsi-dropdown-notch-base-size')) || 18

        // Make the menu as wide as the content block
        menu.style.width = `${contentRect.width}px`

        // Keep the notch horizontally centred above the clicked toggle
        const notchX = toggleRect.left + toggleRect.width / 2 - contentRect.left - notchSize / 2
        menu.style.setProperty('--bsi-dropdown-notch-position-x', `${notchX}px`)

        // Keep the notch protruding 8px above the menu top
        menu.style.setProperty('--bsi-dropdown-notch-position-y', '-8px')

        return [0, 0]
      },
    })
  })
}

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHeaderAudienceDropdowns)
  } else {
    initHeaderAudienceDropdowns()
  }
}

export default initHeaderAudienceDropdowns

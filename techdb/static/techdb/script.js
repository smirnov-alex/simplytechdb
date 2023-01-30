const sectorAkb = document.querySelector('.site__title--akb');
if (sectorAkb != null) {
  const arrowButtonAkb = sectorAkb.querySelector('i');
  const rollupContainerAkb = document.querySelector('.rollup-container-akb');
  sectorAkb.addEventListener('click', () => {
    console.log('hello');
    arrowButtonAkb.classList.toggle('up');
    arrowButtonAkb.classList.toggle('down');
    rollupContainerAkb.classList.toggle('visually-hidden');
  });
}

const sectorQuazar = document.querySelector('.site__title--quazar');
if (sectorQuazar != null) {
  const arrowButtonQuazar = sectorQuazar.querySelector('i');
  const rollupContainerQuazar = document.querySelector('.rollup-container-quazar');

  sectorQuazar.addEventListener('click', () => {
    arrowButtonQuazar.classList.toggle('up');
    arrowButtonQuazar.classList.toggle('down');
    rollupContainerQuazar.classList.toggle('visually-hidden');
  });
}

const sectorOldinfo = document.querySelector('.site__title--oldinfo');
if (sectorOldinfo != null) {
  const arrowButtonOldinfo = sectorOldinfo.querySelector('i');
  const rollupContainerOldinfo = document.querySelector('.rollup-container-oldinfo');

  sectorOldinfo.addEventListener('click', () => {
    arrowButtonOldinfo.classList.toggle('up');
    arrowButtonOldinfo.classList.toggle('down');
    rollupContainerOldinfo.classList.toggle('visually-hidden');
  });
}

const sectorEnergy = document.querySelector('.site__title--energy');
if (sectorEnergy != null) {
  const arrowButtonEnergy = sectorEnergy.querySelector('i');
  const rollupContainerEnergy = document.querySelector('.rollup-container-energy');

  sectorEnergy.addEventListener('click', () => {
    arrowButtonEnergy.classList.toggle('up');
    arrowButtonEnergy.classList.toggle('down');
    rollupContainerEnergy.classList.toggle('visually-hidden');
  });
}

const sectorEquipment = document.querySelector('.site__title--equipment');
if (sectorEquipment != null) {
  const arrowButtonEquipment = sectorEquipment.querySelector('i');
  const rollupContainerEquipment = document.querySelector('.rollup-container-equipment');

  sectorEquipment.addEventListener('click', () => {
    arrowButtonEquipment.classList.toggle('up');
    arrowButtonEquipment.classList.toggle('down');
    rollupContainerEquipment.classList.toggle('visually-hidden');
  });
}

const sectorRrl = document.querySelector('.site__title--rrl');
if (sectorRrl != null) {
  const arrowButtonRrl = sectorRrl.querySelector('i');
  const rollupContainerRrl = document.querySelector('.rollup-container-rrl');

  sectorRrl.addEventListener('click', () => {
    arrowButtonRrl.classList.toggle('up');
    arrowButtonRrl.classList.toggle('down');
    rollupContainerRrl.classList.toggle('visually-hidden');
  });
}

const sitesList = document.querySelector('.site__title--main');
if (sitesList != null) {
  const arrowButtonSites = sitesList.querySelector('i');
  const rollupContainerSites = document.querySelector('.rollup-container-sites');

  sitesList.addEventListener('click', () => {
    arrowButtonSites.classList.toggle('up');
    arrowButtonSites.classList.toggle('down');
    rollupContainerSites.classList.toggle('visually-hidden');
  });
}


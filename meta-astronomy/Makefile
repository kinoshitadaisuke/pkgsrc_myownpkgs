# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-astronomy-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs math science python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for astronomy
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

DEPENDS+=	${PYPKGPREFIX}-asdf>=0:../../pkgsrc_myownpkgs/py-asdf
DEPENDS+=	${PYPKGPREFIX}-asdf-astropy>=0:../../pkgsrc_myownpkgs/py-asdf-astropy
DEPENDS+=	${PYPKGPREFIX}-astroML>=0:../../pkgsrc_myownpkgs/py-astroML
DEPENDS+=	${PYPKGPREFIX}-astroalign>=0:../../pkgsrc_myownpkgs/py-astroalign
DEPENDS+=	${PYPKGPREFIX}-astroplan>=0:../../pkgsrc_myownpkgs/py-astroplan
DEPENDS+=	${PYPKGPREFIX}-astropy>=0:../../pkgsrc_myownpkgs/py-astropy
DEPENDS+=	${PYPKGPREFIX}-astropy-iers-data>=0:../../pkgsrc_myownpkgs/py-astropy-iers-data
DEPENDS+=	${PYPKGPREFIX}-astroquery>=0:../../pkgsrc_myownpkgs/py-astroquery
DEPENDS+=	${PYPKGPREFIX}-de405>=0:../../pkgsrc_myownpkgs/py-de405
DEPENDS+=	${PYPKGPREFIX}-de406>=0:../../pkgsrc_myownpkgs/py-de406
DEPENDS+=	${PYPKGPREFIX}-de421>=0:../../pkgsrc_myownpkgs/py-de421
DEPENDS+=	${PYPKGPREFIX}-de422>=0:../../pkgsrc_myownpkgs/py-de422
DEPENDS+=	${PYPKGPREFIX}-de423>=0:../../pkgsrc_myownpkgs/py-de423
DEPENDS+=	${PYPKGPREFIX}-ginga>=0:../../pkgsrc_myownpkgs/py-ginga
DEPENDS+=	${PYPKGPREFIX}-gwcs>=0:../../pkgsrc_myownpkgs/py-gwcs
DEPENDS+=	${PYPKGPREFIX}-jplephem>=0:../../pkgsrc_myownpkgs/py-jplephem
DEPENDS+=	${PYPKGPREFIX}-photutils>=0:../../pkgsrc_myownpkgs/py-photutils
DEPENDS+=	${PYPKGPREFIX}-pyvo>=0:../../pkgsrc_myownpkgs/py-pyvo
DEPENDS+=	${PYPKGPREFIX}-rebound>=0:../../pkgsrc_myownpkgs/py-rebound
DEPENDS+=	${PYPKGPREFIX}-regions>=0:../../pkgsrc_myownpkgs/py-regions
DEPENDS+=	${PYPKGPREFIX}-sep>=0:../../pkgsrc_myownpkgs/py-sep
DEPENDS+=	${PYPKGPREFIX}-sbpy>=0:../../pkgsrc_myownpkgs/py-sbpy
DEPENDS+=	${PYPKGPREFIX}-skyfield>=0:../../pkgsrc_myownpkgs/py-skyfield
DEPENDS+=	${PYPKGPREFIX}-skyfield-data>=0:../../pkgsrc_myownpkgs/py-skyfield-data
DEPENDS+=	${PYPKGPREFIX}-starplot>=0:../../pkgsrc_myownpkgs/py-starplot
DEPENDS+=	${PYPKGPREFIX}-synphot>=0:../../pkgsrc_myownpkgs/py-synphot
DEPENDS+=	${PYPKGPREFIX}-trippy>=0:../../pkgsrc_myownpkgs/py-trippy
DEPENDS+=	saoimage_ds9-bin>=0:../../pkgsrc_myownpkgs/saoimage_ds9-bin
DEPENDS+=	wcstools>=0:../../pkgsrc_myownpkgs/wcstools
DEPENDS+=	xephem>=0:../../pkgsrc_myownpkgs/xephem

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"

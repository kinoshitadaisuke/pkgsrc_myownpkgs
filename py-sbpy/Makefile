# $NetBSD$

DISTNAME=	sbpy-0.6.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/sbpy/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/sbpy/
COMMENT=	Astropy affiliated package for small-body planetary astronomy
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-numpy>=1.17.0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-astropy>=5.0:../../pkgsrc_myownpkgs/py-astropy
DEPENDS+=	${PYPKGPREFIX}-astroquery>=0.4.5:../../pkgsrc_myownpkgs/py-astroquery
DEPENDS+=	${PYPKGPREFIX}-scipy>0:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-synphot>=1.0.0:../../pkgsrc_myownpkgs/py-synphot

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"

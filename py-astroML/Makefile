# $NetBSD$

DISTNAME=	astroML-1.0.2.post1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/astroML/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/astroML/
COMMENT=	Machine learning for astronomy and astrophysics
LICENSE=	2-clause-bsd

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-setuptools>0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-wheel>0:../../devel/py-wheel
DEPENDS+=	${PYPKGPREFIX}-scikit-learn>=0.18:../../math/py-scikit-learn
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.13:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-scipy>=0.19:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=3.0:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-astropy>=3.0:../../pkgsrc_myownpkgs/py-astropy
DEPENDS+=	${PYPKGPREFIX}-pymc3>=3.7:../../math/py-pymc3

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
